import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import sys
import copy
import functools
import time
import random
sys.setrecursionlimit(10 ** 7)
inf = 10 ** 20
eps = 1.0 / 10 ** 10
mod = 10 ** 9 + 7
mod2 = 998244353
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def LI():
    return list(map(int, sys.stdin.readline().split()))


def LLI():
    return [list(map(int, l.split())) for l in sys.stdin.readlines()]


def LI_():
    return [int(x) - 1 for x in sys.stdin.readline().split()]


def LF():
    return [float(x) for x in sys.stdin.readline().split()]


def LS():
    return sys.stdin.readline().split()


def I():
    return int(sys.stdin.readline())


def F():
    return float(sys.stdin.readline())


def S():
    return input()


def pf(s):
    return print(s, flush=True)


def pe(s):
    return print(str(s), file=sys.stderr)


def JA(a, sep):
    return sep.join(map(str, a))


def JAA(a, s, t):
    return s.join((t.join(map(str, b)) for b in a))


def main():
    n = I()
    a = LI()
    if n < 4:
        return max(a)
    dp = [[-inf] * 3 for _ in range(n)]
    for i in range(3):
        dp[i][i] = a[i]
    for i in range(n):
        c = a[i]
        di = dp[i]
        if i > 1:
            d2 = dp[i - 2]
            for j in range(3):
                if di[j] < d2[j] + c:
                    di[j] = d2[j] + c
        if i > 2:
            d3 = dp[i - 3]
            for j in range(2):
                if di[j + 1] < d3[j] + c:
                    di[j + 1] = d3[j] + c
        if i > 3:
            d4 = dp[i - 4]
            for j in range(1):
                if di[j + 2] < d4[j] + c:
                    di[j + 2] = d4[j] + c
    if n % 2 == 0:
        return max(dp[-1][1], dp[-2][0])
    r = -inf
    for i in range(3):
        r = max(r, dp[-1 - i][2 - i])
    return r


print(main())
