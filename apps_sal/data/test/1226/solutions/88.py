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
    (N, a, b) = [int(x) for x in input().split()]

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
    print((MOD + pow(2, N, MOD) - 1 - coef(N, a) - coef(N, b)) % MOD)


T = 1
for case in range(1, T + 1):
    ans = solve()
'\n\n\n\n\n'
