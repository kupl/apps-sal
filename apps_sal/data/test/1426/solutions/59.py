from heapq import heappop, heappush, heapify

INF = float("inf")
n, m = list(map(int, input().split()))
idx = [[i * 3 + j for j in range(3)] for i in range(n)]
g = [[] for _ in range(n * 3)]
for _ in range(m):
    u, v = [int(x) - 1 for x in input().split()]
    for i in range(3):
        g[idx[u][i]].append((idx[v][(i + 1) % 3], 1))
s, t = [int(x) - 1 for x in input().split()]


def dijkstra(graph, n, s):
    d = [INF] * n
    d[s], q = 0, []
    heappush(q, (0, s))
    while q:
        dist, v = heappop(q)
        if d[v] < dist:
            continue
        for nv, cost in graph[v]:
            if d[nv] > d[v] + cost:
                d[nv] = d[v] + cost
                heappush(q, (d[nv], nv))
    return d


res = dijkstra(g, n * 3, idx[s][0])[idx[t][0]]
print((-1 if res == INF else res // 3))
