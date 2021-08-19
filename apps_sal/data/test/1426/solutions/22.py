from collections import deque
import sys
input = sys.stdin.readline
(n, m) = list(map(int, input().split()))
UV = [[] for _ in range(n)]
for _ in range(m):
    (u, v) = list([int(x) - 1 for x in input().split()])
    UV[u].append(v)
(s, t) = list([int(x) - 1 for x in input().split()])
NV = 3 * n
edges = [[] for _ in range(NV)]


def to_v(i, j):
    return 3 * i + j


for i in range(n):
    for i2 in UV[i]:
        for j in range(3):
            edges[to_v(i, j)].append(to_v(i2, (j + 1) % 3))
init_v = to_v(s, 0)
INF = 10 ** 18
dist = [INF] * NV
dist[init_v] = 0
next_v = deque([init_v])
while next_v:
    v = next_v.popleft()
    for v2 in edges[v]:
        if dist[v2] <= dist[v] + 1:
            continue
        dist[v2] = dist[v] + 1
        next_v.append(v2)
print(dist[to_v(t, 0)] // 3 if dist[to_v(t, 0)] != INF else -1)
