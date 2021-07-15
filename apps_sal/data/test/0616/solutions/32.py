import sys
import re
import math
import collections
import decimal
import bisect
import itertools
import fractions
import functools
import copy
import heapq
import decimal
import statistics
import queue

# import numpy as np

sys.setrecursionlimit(10 ** 9)
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline())
ns = lambda: list(map(int, sys.stdin.readline().split()))
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===

def main():
    n, m = ns()
    d = []
    for _ in range(m):
        ai, bi = ns()
        ci = na()
        d.append([ai, bi, ci])

    # bit DP
    # dp[i] = iの各bitが1である番目の宝箱を開けられる状態となれる最小コスト
    dp = [INF for _ in range(2 ** n)]
    dp[0] = 0

    for ai, bi, ci in d:
        getkey = 0
        for cii in ci:
            cii -= 1
            getkey += 1 << cii

        for i in range(2 ** n):
            dp[i | getkey] = min(dp[i | getkey], dp[i] + ai)

    tmp = dp[2 ** n - 1]
    print((tmp if tmp != INF else -1))


def __starting_point():
    main()

__starting_point()
