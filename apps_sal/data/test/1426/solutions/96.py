from sys import stdin
from collections import deque


def input():
    return stdin.readline().strip()


def bfs():
    q = deque([S])
    dist = [-1] * (3 * N)
    dist[S] = 0
    while q:
        v = q.popleft()
        for nv in g[v]:
            if dist[nv] >= 0:
                continue
            dist[nv] = dist[v] + 1
            q.append(nv)
    return dist[T] // 3


(N, M) = list(map(int, input().split()))
g = [[] for _ in range(3 * N)]
for _ in range(M):
    (a, b) = [int(x) - 1 for x in input().split()]
    g[3 * a].append(3 * b + 1)
    g[3 * a + 1].append(3 * b + 2)
    g[3 * a + 2].append(3 * b)
(S, T) = [3 * (int(x) - 1) for x in input().split()]
print(bfs())
