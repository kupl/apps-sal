import heapq
import itertools


def dijkstra(s):
    inf = pow(10, 10)
    dist = [inf] * (n + 1)
    dist[s] = 0
    c = [0] * (n + 1)
    p = []
    heapq.heapify(p)
    heapq.heappush(p, (dist[s], s))
    while p:
        d, u = heapq.heappop(p)
        if dist[u] < d:
            continue
        c[u] = 1
        for g in G[u]:
            if c[g[0]] == 0 and dist[u] + g[1] < dist[g[0]]:
                dist[g[0]] = dist[u] + g[1]
                heapq.heappush(p, (dist[g[0]], g[0]))
    return dist


n, m, r = map(int, input().split())
t = list(map(int, input().split()))
G = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    G[a].append([b, c])
    G[b].append([a, c])
D = [[0] * r for _ in range(r)]
for i in range(r):
    d = dijkstra(t[i])
    for j in range(r):
        D[i][j] = d[t[j]]

x = [i for i in range(r)]
ans = pow(10, 10)
for y in itertools.permutations(x):
    dist = 0
    y = list(y)
    for i in range(r - 1):
        dist += D[y[i]][y[i + 1]]
    ans = min(ans, dist)
print(ans)
