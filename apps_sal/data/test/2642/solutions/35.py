from collections import defaultdict
from fractions import Fraction
import bisect
import math
from pprint import pformat as pf
from pprint import pprint as pp
import sys
sys.setrecursionlimit(10 ** 7)


def is_same_sign(a, b):
    if a > 0 and b > 0:
        return True
    if a < 0 and b < 0:
        return True
    return False


def fraction_taple(a, b):
    g = math.gcd(a, b)
    if is_same_sign(a, b):
        s = 1
    else:
        s = -1
    a = abs(a) // g
    b = abs(b) // g
    return (s, a, b)


def mode(a, b):
    if a == 0 and b == 0:
        return (0, 0)
    if a == 0:
        return ('ab', 0)
    if b == 0:
        return ('ab', 1)
    x = fraction_taple(a, b)
    y = fraction_taple(-1 * b, a)
    if x > y:
        return (x, 0)
    else:
        return (y, 1)


MOD = 1000000007


def __starting_point():
    n = int(input())
    d = defaultdict(lambda: [0, 0])
    zero = 0
    for _ in range(n):
        (a, b) = list(map(int, input().split()))
        (dkey, akey) = mode(a, b)
        if dkey == 0:
            zero += 1
        else:
            d[dkey][akey] += 1
    ans = 1
    for pair in list(d.values()):
        tmp = pow(2, pair[0], MOD) - 1 + pow(2, pair[1], MOD) - 1 + 1
        ans *= tmp
    ans += zero - 1
    ans %= MOD
    print(ans)


__starting_point()
