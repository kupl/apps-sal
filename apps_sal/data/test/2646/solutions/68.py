from collections import deque

N, M = map(int, input().split())
dist = [-1] * N
dist[0] = 0
prv = [0] * N
G = [[] for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

d = deque()
d.append(0)

while d:
    now = d.popleft()
    for nv in G[now]:
        if dist[nv] == -1:
            dist[nv] = dist[now] + 1
            prv[nv] = now
            d.append(nv)

print("Yes")
for p in prv[1:]:
    print(p + 1)
