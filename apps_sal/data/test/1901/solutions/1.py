# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2017/11/23 23:13

"""

N, M = list(map(int, input().split()))
cost = [0] + [int(x) for x in input().split()]
#
# N, M = random.randint(1, 10**5), random.randint(0, 10**5)
# cost = [0] + [random.randint(0, 10**9) for _ in range(N)]

G = collections.defaultdict(list)

for i in range(M):
    a, b = list(map(int, input().split()))
    # a, b = random.randint(1, N), random.randint(1, N)
    G[a].append(b)
    G[b].append(a)


group = [0] * (N + 1)
gi = 1

# def dfs(u, fa, gi):
#     group[u] = gi
#     for v in G[u]:
#         if v != fa and group[v] == 0:
#             dfs(v, u, gi)


def makeGroup(u, gi):
    q = [u]
    while q:
        u = q.pop()
        group[u] = gi
        for v in G[u]:
            if group[v] == 0:
                q.append(v)


for i in range(1, N + 1):
    if not group[i]:
        gi += 1
        makeGroup(i, gi)

for i in range(1, N + 1):
    if group[i] == 0:
        gi += 1
        group[i] = gi

minCost = {}
for i in range(1, N + 1):
    g = group[i]
    c = cost[i]
    if g not in minCost:
        minCost[g] = c
    else:
        minCost[g] = min(minCost[g], c)

print(sum(list(minCost.values()) or [0]))
