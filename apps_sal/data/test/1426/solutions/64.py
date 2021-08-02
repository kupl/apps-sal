from sys import stdin
from collections import deque


def input():
    return stdin.readline().strip()


def bfs():
    q = deque([3 * S])
    dist = [-1] * (3 * N)
    dist[3 * S] = 0
    while q:
        p = q.popleft()
        v, r = divmod(p, 3)
        nr = (r + 1) % 3
        for nv in g[v]:
            np = 3 * nv + nr
            if dist[np] >= 0:
                continue
            dist[np] = dist[p] + 1
            q.append(np)
    return dist[3 * T] // 3


N, M = list(map(int, input().split()))
g = [[] for _ in range(N)]
for _ in range(M):
    a, b = [int(x) - 1 for x in input().split()]
    g[a].append(b)
S, T = [int(x) - 1 for x in input().split()]
print((bfs()))
