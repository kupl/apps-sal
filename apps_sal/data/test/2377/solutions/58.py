from functools import lru_cache, reduce
from bisect import bisect_left, bisect_right
import random
import operator
import string
import sys
from collections import deque, defaultdict, namedtuple
import heapq
from math import sqrt, factorial, gcd, ceil, atan, pi
def input(): return sys.stdin.readline()[:-1]


MOD = int(1e9) + 7
INF = float('inf')


def solve():
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
for case in range(1, T + 1):
    ans = solve()


"""

dp[num_changes][blue_placed]


abba

(m + 1)

"""
