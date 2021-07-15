import sys
from collections import deque


def input():
    return sys.stdin.readline().strip()


def bfs(start):
    q = deque([start])
    dist = [-1] * (N + 1)
    dist[start] = 0
    while q:
        v = q.popleft()
        for nv, nw in g[v]:
            if dist[nv] > 0:
                continue
            dist[nv] = dist[v] + nw
            q.append(nv)
    return dist


N = int(input())
g = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, c = list(map(int, input().split()))
    g[a].append((b, c))
    g[b].append((a, c))
Q, K = list(map(int, input().split()))
d = bfs(K)
ans = []
for _ in range(Q):
    x, y = list(map(int, input().split()))
    print((d[x] + d[y]))

