# -*- coding: utf-8 -*-
from functools import lru_cache, reduce
from bisect import bisect_left, bisect_right
import random
import operator
import string
import sys
from collections import deque, defaultdict, namedtuple
import heapq
from math import sqrt, factorial, gcd, ceil, atan, pi
def input(): return sys.stdin.readline()[:-1]  # warning not \n


# def input(): return sys.stdin.buffer.readline()[:-1] # warning bytes
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8').strip()
# string.ascii_lowercase
MOD = int(1e9) + 7
INF = float('inf')


def print_lines(data):
    sys.stdout.write('\n'.join((str(x) for x in data)))


def solve():
    X, Y = [int(x) for x in input().split()]

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
        return (prod(n - k + 1, n) * pow(fact(k) % MOD, MOD - 2, MOD)) % MOD

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
# T = int(input())
for case in range(1, T + 1):
    ans = solve()


"""

1 2
3 4
4 6

x (1, 2) + y (2, 1)

x + 2y = X
2x + y = Y

2x + 4y = 2X
-2x - y = -Y
3y = 2X - Y
y = (2 * X - Y)


3 3


2 1


"""
