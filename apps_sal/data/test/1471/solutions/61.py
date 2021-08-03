#!/usr/bin/env python3
from collections import deque

n = int(input())
g = [list() for _ in range(n)]
visited = [True] * n
coler = [0] * n
for _ in range(1, n):
    v1, v2, w = map(int, input().split())
    v1 -= 1
    v2 -= 1
    w %= 2
    g[v1].append((v2, w))
    g[v2].append((v1, w))

q = deque([0])
visited[0] = False
while q:
    a = q.pop()
    for v, w in g[a]:
        if visited[v]:
            visited[v] = False
            coler[v] = (coler[a] + w) % 2
            q.append(v)

print(*coler, sep="\n")
