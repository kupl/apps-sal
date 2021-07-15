#!/usr/bin/env python
from collections import deque

# input
n, m = list(map(int, input().split()))
a = [0 for _ in range(m)]
b = [0 for _ in range(m)]
for i in range(m):
    a[i], b[i] = list(map(int, input().split()))

if m == 1:
    print('IMPOSSIBLE')
    return

to = [[] for _ in range(n+1)]
for i in range(m):
    to[a[i]].append(b[i])
    to[b[i]].append(a[i])
#print('to =', to)

# BFS
inf = 200200
dist = [inf for _ in range(n+1)]
q = deque()
q.append(1)
dist[1] = 0 

while q:
    v = q.popleft()
    for u in to[v]:
        if dist[u] == inf:
            dist[u] = dist[v]+1
            q.append(u)

if dist[n] == 2:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')

