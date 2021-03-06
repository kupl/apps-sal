from functools import lru_cache, reduce
from bisect import bisect_left, bisect_right
import operator
import string
import sys
from collections import deque, defaultdict, namedtuple
from math import sqrt, factorial, gcd, ceil, atan, pi


def input():
    return sys.stdin.readline()[:-1]


MOD = int(1000000000.0) + 7
INF = float('inf')


def solve():
    (a, n, m) = [int(x) for x in input().split()]
    rain = [0] * (a + 1)
    for _ in range(n):
        (l, r) = [int(x) for x in input().split()]
        for i in range(l + 1, r + 1):
            rain[i] = 1
    umb = []
    for _ in range(m):
        (x, p) = [int(x) for x in input().split()]
        umb.append((x, p))
    umb.sort()
    dp = [INF for _ in range(a + 1)]
    dp[0] = 0
    for i in range(1, a + 1):
        if rain[i]:
            for (x, p) in umb:
                if x >= i:
                    break
                dp[i] = min(dp[i], dp[x] + p * (i - x))
        else:
            dp[i] = dp[i - 1]
    if dp[a] == INF:
        print(-1)
    else:
        print(dp[a])


t = 1
for case in range(1, t + 1):
    ans = solve()
'\n\n1 2\n\ndp[x] = min()\n\n\n\n\n'
