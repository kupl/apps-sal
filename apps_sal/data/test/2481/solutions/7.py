# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict, namedtuple
import heapq
from math import sqrt, factorial, gcd, ceil, atan, pi
def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline()[:-1] # warning bytes
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8').strip()
import string
import operator
import random
# string.ascii_lowercase
from bisect import bisect_left, bisect_right
from functools import lru_cache, reduce
MOD = int(1e9)+7
INF = float('inf')


def solve():
    n, m = [int(x) for x in input().split()]
    p = []
    for _ in range(10):
        p.append([int(x) for x in input().split()])

    stack = set()
    def dfs(v):
        if v == 1:
            return 0
        stack.add(v)
        for to in range(10):
            if to == v or to in stack: continue
            if p[v][to] < p[v][1]:
                p[v][1] = min(p[v][1], dfs(to) + p[v][to])
        stack.remove(v)
        return p[v][1]

    for i in range(10):
        dfs(i)

    ans = 0
    for _ in range(n):
        row = [int(x) for x in input().split()]
        for e in row:
            if e == -1 or e == 1: continue
            ans += p[e][1]
    print(ans)



T = 1
# T = int(input())
for case in range(1,T+1):
    ans = solve()


"""

dp[num_changes][blue_placed]


abba



"""

