import sys
import math
import collections
import bisect
import itertools
import fractions
import copy
import decimal
import queue
from functools import reduce


sys.setrecursionlimit(10000001)
INF = 10 ** 16
MOD = 10 ** 9 + 7


def ni(): return int(sys.stdin.readline())
def ns(): return list(map(int, sys.stdin.readline().split()))
def na(): return list(map(int, sys.stdin.readline().split()))


def main():
    from functools import reduce

    def lcm_base(x, y):
        return (x * y) // math.gcd(x, y)

    def lcm_list(numbers):
        return reduce(lcm_base, numbers, 1)

    n = ni()
    a = na()

    lcm = a[0]
    for i in a:
        lcm = lcm // math.gcd(lcm, i) * i
    lcm %= MOD

    ans = 0
    for ai in a:
        ans += lcm * pow(ai, MOD - 2, MOD) % MOD
        ans %= MOD

    print(ans)


def __starting_point():
    main()


__starting_point()
