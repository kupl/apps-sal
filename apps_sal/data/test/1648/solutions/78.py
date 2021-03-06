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


class Combination:

    def __init__(self, n_max, mod=10 ** 9 + 7):
        self.mod = mod
        f = 1
        self.fac = fac = [f]
        for i in range(1, n_max + 1):
            f = f * i % mod
            fac.append(f)
        f = pow(f, mod - 2, mod)
        self.facinv = facinv = [f]
        for i in range(n_max, 0, -1):
            f = f * i % mod
            facinv.append(f)
        facinv.reverse()

    def __call__(self, n, r):
        return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n - r] % self.mod

    def nCr(self, n, r):
        if not 0 <= r <= n:
            return 0
        return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n - r] % self.mod


def solve():
    (total, blue) = [int(x) for x in input().split()]
    red = total - blue

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
        return fact(n) * pow(fact(k) * fact(n - k) % MOD, MOD - 2, MOD) % MOD
    for i in range(1, blue + 1):
        print(coef(red + 1, i) * coef(blue - 1, i - 1) % MOD)


T = 1
for case in range(1, T + 1):
    ans = solve()
'\n\ndp[num_changes][blue_placed]\n\n\nabba\n\n(m + 1)\n\n'
