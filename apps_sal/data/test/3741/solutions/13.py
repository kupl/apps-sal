import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List
'\ncreated by shhuan at 2020/1/10 01:32\n\n'


def shortest_path(u, v, g):
    q = [w for w in g[u] if w != v]
    vis = set(q) | {u}
    d = 0
    while q:
        d += 1
        nq = []
        for w in q:
            if w == v:
                return d
            for x in g[w]:
                if x not in vis:
                    vis.add(x)
                    nq.append(x)
        q = nq
    return float('inf')


def solve(N, A):
    b = 1
    g = collections.defaultdict(list)
    edges = []
    for i in range(64):
        connected = [i for (i, v) in enumerate(A) if v & b > 0]
        if len(connected) >= 3:
            return 3
        for u in connected:
            for v in connected:
                if u != v:
                    g[u].append(v)
                    edges.append((u, v))
        b <<= 1
    ans = float('inf')
    for (u, v) in edges:
        ans = min(ans, 1 + shortest_path(u, v, g))
    return ans if ans < float('inf') else -1


N = int(input())
A = [int(x) for x in input().split()]
print(solve(N, A))
