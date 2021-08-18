import sys
import re
import math
import collections
import bisect
import itertools
import fractions
import functools
import copy
import heapq
import decimal
import statistics
import queue


sys.setrecursionlimit(10 ** 9)
INF = 10 ** 16
MOD = 10 ** 9 + 7


def ni(): return int(sys.stdin.readline())
def ns(): return list(map(int, sys.stdin.readline().split()))
def na(): return list(map(int, sys.stdin.readline().split()))
def nb(): return list([int(x) - 1 for x in sys.stdin.readline().split()])


def main():
    s = list(input())
    l = len(s)
    dp1 = [0 for _ in range(l + 1)]
    dp2 = [0 for _ in range(l + 1)]
    dp1[0] = 1

    for i in range(l):
        if s[i] == "1":
            dp1[i + 1] = dp1[i] * 2
            dp2[i + 1] = dp1[i] + dp2[i] * 3
        else:
            dp1[i + 1] = dp1[i]
            dp2[i + 1] = dp2[i] * 3
        dp1[i + 1] %= MOD
        dp2[i + 1] %= MOD

    print(((dp1[l] + dp2[l]) % MOD))


def __starting_point():
    main()


__starting_point()
