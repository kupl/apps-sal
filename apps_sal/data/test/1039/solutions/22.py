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
sys.setrecursionlimit(int(1000000.0))


def solve():
    n = int(input())
    g = defaultdict(list)
    for _ in range(n - 1):
        (a, b, c) = [int(x) for x in input().split()]
        g[a].append((b, c))
        g[b].append((a, c))
    (q, k) = [int(x) for x in input().split()]
    d = defaultdict(int)

    def dfs(v, f, dis):
        d[v] = dis
        for (to, xd) in g[v]:
            if to == f:
                continue
            dfs(to, v, dis + xd)
    dfs(k, -1, 0)
    for _ in range(q):
        (a, b) = [int(x) for x in input().split()]
        print(d[a] + d[b])


T = 1
for case in range(1, T + 1):
    ans = solve()
'\n\ndp[num_changes][blue_placed]\n\n\nabba\n\n\n\n'
