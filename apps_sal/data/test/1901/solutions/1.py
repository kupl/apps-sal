
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

G = collections.defaultdict(list)

for i in range(M):
    a, b = list(map(int, input().split()))
    G[a].append(b)
    G[b].append(a)


group = [0] * (N + 1)
gi = 1


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
