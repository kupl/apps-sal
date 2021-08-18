from bisect import bisect_left, bisect_right
from fractions import Fraction
from collections import defaultdict
import sys
input = sys.stdin.readline


def read():
    N = int(input().strip())
    AB = []
    ZAB = []
    M = 0
    ZM = 0
    for i in range(N):
        a, b = map(int, input().strip().split())
        if a != 0 or b != 0:
            AB.append((a, b))
            M += 1
    return N, M, AB


def solve(N, M, AB, MOD=1000000007):
    D = defaultdict(int)
    INVD = defaultdict(int)

    keys = set()
    for a, b in AB:
        if a == 0:
            D["0"] += 1
            keys.add("0")
        elif b == 0:
            INVD["0"] += 1
            keys.add("0")
        else:
            f = Fraction(a, b)
            if f > 0:
                key = str(f)
                D[key] += 1
                keys.add(key)
            else:
                key = str(-1 / f)
                INVD[key] += 1
                keys.add(key)

    ans = 1
    for key in keys:
        g1 = pow(2, D[key], MOD) - 1
        g2 = pow(2, INVD[key], MOD) - 1
        g3 = 1
        ans *= (g1 + g2 + g3)
        ans %= MOD

    ans -= 1
    ans %= MOD

    ans += N - M
    ans %= MOD

    return ans


def __starting_point():
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))


__starting_point()
