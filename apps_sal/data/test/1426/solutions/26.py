from sys import stdin
from collections import deque


def input():
    return stdin.readline().strip()


def bfs():
    q = deque([(S, 0)])
    dist = [[-1] * 3 for _ in range(N)]
    dist[S][0] = 0
    while q:
        (v, r) = q.popleft()
        for nv in g[v]:
            nr = (r + 1) % 3
            if dist[nv][nr] >= 0:
                continue
            dist[nv][nr] = dist[v][r] + 1
            q.append((nv, nr))
    return dist[T][0] // 3


(N, M) = list(map(int, input().split()))
g = [[] for _ in range(3 * N)]
for _ in range(M):
    (a, b) = [int(x) - 1 for x in input().split()]
    g[a].append(b)
(S, T) = [int(x) - 1 for x in input().split()]
print(bfs())
