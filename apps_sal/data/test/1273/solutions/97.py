from math import ceil, floor, factorial, gcd, sqrt, log2, cos, sin, tan, acos, asin, atan, degrees, radians, pi, inf
from itertools import accumulate, groupby, permutations, combinations, product, combinations_with_replacement
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
from operator import itemgetter
from heapq import heapify, heappop, heappush
from queue import Queue, LifoQueue, PriorityQueue
from copy import deepcopy
from time import time
from functools import reduce
import string
import sys
sys.setrecursionlimit(10 ** 7)
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def MAP1(): return map(lambda x: int(x) - 1, input().split())
def LIST(): return list(MAP())


def solve():
    n = INT()
    Q = [tuple(MAP1()) for _ in range(n - 1)]

    deg = [0] * n
    adj = [[] for _ in range(n)]
    color = dict()

    for a, b in Q:
        deg[a] += 1
        deg[b] += 1
        adj[a].append(b)
        adj[b].append(a)

    def dfs(s, p):
        nouse = -1
        if p > -1:
            nouse = color[(min(s, p), max(s, p))]
        c = 1
        for t in adj[s]:
            if t == p:
                continue
            if c == nouse:
                c += 1
            color[(min(s, t), max(s, t))] = c
            dfs(t, s)
            c += 1

    dfs(1, -1)

    print(max(deg))
    for a, b in Q:
        print(color[(a, b)])


def __starting_point():
    solve()


__starting_point()
