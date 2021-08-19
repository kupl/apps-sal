#!/usr/bin/env python3
from collections import deque

INF = 10**9
k = int(input())

# (辺の伸びる先, コスト)
G = [((10 * i % k, 0), ((i + 1) % k, 1)) for i in range(k)]
s = 1

# 01 - BFS
dist = [INF] * k
S = deque([s])
T = deque()
dist[s] = 0

d = 0
while S:
    while S:
        v = S.popleft()
        for w, c in G[v]:
            if d + c < dist[w]:
                dist[w] = d + c
                if c:
                    T.append(w)
                else:
                    S.append(w)
    S, T = T, S
    d += 1

print(dist[0] + 1)
