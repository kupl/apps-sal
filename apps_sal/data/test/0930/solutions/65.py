import sys
# import re
import math
import collections
# import decimal
import bisect
import itertools
import fractions
# import functools
import copy
# import heapq
import decimal
# import statistics
import queue

# import numpy as np

sys.setrecursionlimit(10000001)
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline())
ns = lambda: list(map(int, sys.stdin.readline().split()))
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===
def main():
    # nCrの左項にはn以外も来るバージョン、1!～(n-1)!を保持
    def prepare(n, MOD):
        # 1! - n! の計算
        f = 1
        factorials = [1]  # 0!の分
        for m in range(1, n + 1):
            f *= m
            f %= MOD
            factorials.append(f)
        # n!^-1 の計算
        inv = pow(f, MOD - 2, MOD)
        # n!^-1 - 1!^-1 の計算
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
