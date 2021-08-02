from collections import deque


N, M, *uv, S, T = list(map(int, open(0).read().split()))
g = [[] for _ in range(N)]
for u, v in zip(*[iter(uv)] * 2):
    g[u - 1].append(v - 1)
S -= 1
T -= 1

q = deque([(S, 0)])
dist = [[-1, -1, -1] for _ in range(N)]
dist[S][0] = 0
r = 0
while q:
    v, r = q.popleft()
    nr = (r + 1) % 3
    for nv in g[v]:
        if dist[nv][nr] >= 0:
            continue
        dist[nv][nr] = dist[v][r] + 1
        q.append((nv, nr))
print((dist[T][0] // 3))
