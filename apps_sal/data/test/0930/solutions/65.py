import sys
import math
import collections
import bisect
import itertools
import fractions
import copy
import decimal
import queue


sys.setrecursionlimit(10000001)
INF = 10 ** 16
MOD = 10 ** 9 + 7


def ni(): return int(sys.stdin.readline())
def ns(): return list(map(int, sys.stdin.readline().split()))
def na(): return list(map(int, sys.stdin.readline().split()))


def main():
    def prepare(n, MOD):
        f = 1
        factorials = [1]
        for m in range(1, n + 1):
            f *= m
            f %= MOD
            factorials.append(f)
        inv = pow(f, MOD - 2, MOD)
        invs = [1] * (n + 1)
        invs[n] = inv
        for m in range(n, 1, -1):
            inv *= m
            inv %= MOD
            invs[m - 1] = inv

        return factorials, invs

    n, k = ns()
    facts, invs = prepare(n, MOD)

    ans = 0
    for ki in range(min(n, k + 1)):
        zero_comb = facts[n] * invs[ki] * invs[n - ki] % MOD
        nonzero_comb = facts[n - 1] * invs[ki] * invs[n - 1 - ki] % MOD
        ans += zero_comb * nonzero_comb % MOD
        ans %= MOD

    print(ans)


def __starting_point():
    main()


__starting_point()
