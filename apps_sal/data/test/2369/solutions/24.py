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


def ni(): return int(sys.stdin.readline())
def ns(): return list(map(int, sys.stdin.readline().split()))
def na(): return list(map(int, sys.stdin.readline().split()))


# ===CODE===
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


def main():
    n, k = ns()
    facts, invs = prepare(n, MOD)

    a = na()
    a.sort()

    ans = 0
    for i, ai in enumerate(a):
        tmp_min = 0
        tmp_max = 0
        if n - i > k - 1:
            min_n = n - i - 1
            min_r = k - 1
            tmp_min = ai * facts[min_n] * invs[min_r] * invs[min_n - min_r] % MOD

        if i + 1 > k - 1:
            max_n = i
            max_r = k - 1
            tmp_max = ai * facts[max_n] * invs[max_r] * invs[max_n - max_r] % MOD

        ans -= tmp_min
        ans += tmp_max
        ans %= MOD

    print(ans)


def __starting_point():
    main()


__starting_point()
