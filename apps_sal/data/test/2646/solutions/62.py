import keyword
from collections import deque

N, M = list(map(int, input().split()))

G = [[] for _ in range(N)]
for i in range(M):
    a, b = list(map(int, input().split()))
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

visited = [False] * N
par = [0] * N
visited[0] = True
d = deque(G[0])
for i in G[0]:
    visited[i] = True
    par[i] = 0
cur = 0
while d:
    cur = d.popleft()
    for i in G[cur]:
        if not visited[i]:
            visited[i] = True
            par[i] = cur
            d.append(i)

print('Yes')
for i in range(1, N):
    print((par[i] + 1))
