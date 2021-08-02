import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import sys
import random
import time
import copy
import bisect
from operator import itemgetter
from heapq import heappush, heappop

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

stdin = sys.stdin

ni = lambda: int(ns())
nf = lambda: float(ns())
na = lambda: list(map(int, stdin.readline().split()))
nb = lambda: list(map(float, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces


def dijkstra(s, n):  # (始点, ノード数)
    dist = [inf] * n
    hq = [(0, s)]  # (distance, node)
    dist[s] = 0
    seen = [False] * n  # ノードが確定済みかどうか
    while hq:
        v = heappop(hq)[1]  # ノードを pop する
        seen[v] = True
        for to, cost in adj[v]:  # ノード v に隣接しているノードに対して
            if seen[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
    return dist


N = ni()
adj = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b, c = na()
    adj[a - 1].append((b - 1, c))
    adj[b - 1].append((a - 1, c))

Q, K = na()
ans = []
d = dijkstra(K - 1, N)

for i in range(Q):
    x, y = na()
    x -= 1
    y -= 1
    ans.append(d[x] + d[y])

for i in range(Q):
    print((ans[i]))
