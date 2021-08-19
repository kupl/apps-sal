from functools import lru_cache, reduce
from bisect import bisect_left, bisect_right
import random
import operator
import string
import sys
from collections import deque, defaultdict, namedtuple
import heapq
from math import sqrt, factorial, gcd, ceil, atan, pi


def input():
    return sys.stdin.readline()[:-1]


MOD = int(1000000000.0) + 7
INF = float('inf')


def print_lines(data):
    sys.stdout.write('\n'.join((str(x) for x in data)))


def solve():
    (X, Y) = [int(x) for x in input().split()]

    def prod(a, b):
        ans = 1
        for x in range(a, b + 1):
            ans *= x
            ans %= MOD
        return ans

    def fact(x):
        ans = 1
        while x:
            ans *= x
            ans %= MOD
            x -= 1
        return ans

    def coef(n, k):
        if k > n:
            return 0
        return prod(n - k + 1, n) * pow(fact(k) % MOD, MOD - 2, MOD) % MOD
    ans = 0
    if (X + Y) % 3 == 0:
        y = (2 * X - Y) // 3
        x = X - 2 * y
        if y >= 0 and x >= 0:
            if x == 0 or y == 0:
                ans = 1
            else:
                ans = coef(x + y, x)
    print(ans)


T = 1
for case in range(1, T + 1):
    ans = solve()
'\n\n1 2\n3 4\n4 6\n\nx (1, 2) + y (2, 1)\n\nx + 2y = X\n2x + y = Y\n\n2x + 4y = 2X\n-2x - y = -Y\n3y = 2X - Y\ny = (2 * X - Y)\n\n\n3 3\n\n\n2 1\n\n\n'
