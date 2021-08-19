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
# def input(): return sys.stdin.buffer.readline().decode('utf-8')
# string.ascii_lowercase
MOD = int(1e9) + 7
INF = float('inf')

# sys.setrecursionlimit(int(1e6))


def solve():
    # n = int(input())
    n, H = [int(x) for x in input().split()]
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = [int(x) for x in input().split()]

    mx = max(a)
    b.sort(reverse=True)
    ans = (H + mx - 1) // mx
    pref = 0

    for i in range(n):
        pref += b[i]
        cur = i + 1 + (max(0, H - pref) + mx - 1) // mx
        ans = min(ans, cur)
    print(ans)


T = 1
# T = int(input())
for case in range(1, T + 1):
    ans = solve()


"""

dp[num_changes][blue_placed]


abba

(m + 1)

"""
