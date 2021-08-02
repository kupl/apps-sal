from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
UV = [tuple(map(int, input().split())) for i in range(M)]
S, T = map(int, input().split())
S, T = S - 1, T - 1

es = [[] for _ in range(N * 3)]
for u, v in UV:
    u, v = u - 1, v - 1
    es[u].append(v + N)
    es[u + N].append(v + N + N)
    es[u + N + N].append(v)

q = deque([S])
INF = float('inf')
dist = [INF] * (N * 3)
dist[S] = 0
while q:
    v = q.popleft()
    for to in es[v]:
        if dist[to] <= dist[v] + 1:
            continue
        dist[to] = dist[v] + 1
        q.append(to)
        if to == T:
            print(dist[to] // 3)
            return
print(-1)
