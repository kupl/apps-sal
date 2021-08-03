from collections import deque
n, m = list(map(int, input().split()))
edges = [[] for i in range(3 * n)]
for i in range(m):
    u, v = list(map(int, input().split()))
    u -= 1
    v -= 1
    edges[u].append(v + n)
    edges[u + n].append(v + 2 * n)
    edges[u + 2 * n].append(v)

s, t = list(map(int, input().split()))
s -= 1
t -= 1
INF = 1 << 50
dists = [INF] * (3 * n)

q = deque([])
q.append(s)
dists[s] = 0

while len(q) > 0:
    v = q.popleft()
    for u in edges[v]:
        if dists[u] != INF:
            continue
        q.append(u)
        dists[u] = dists[v] + 1

if dists[t] == INF:
    print((-1))
else:
    print((dists[t] // 3))
