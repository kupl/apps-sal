from heapq import heappush, heappop
INF = 10**20


def dijkstra(G, start=0):
    d = [INF for i in range(len(G))]
    d[start] = 0
    prev = [0 for i in range(len(G))]

    que = []
    heappush(que, (0, start))

    while len(que) != 0:
        p = heappop(que)
        v = p[1]

        if d[v] < p[0]:
            continue

        for u in G[v].keys():
            if d[u] > d[v] + G[v][u]:
                d[u] = d[v] + G[v][u]
                prev[u] = v
                heappush(que, (d[u], u))

    return d, prev


N, M = map(int, input().split())
G = [{} for _ in range(N + 1)]

edgelist = []
for i in range(M):
    a, b, c = map(int, input().split())
    G[a][b] = G[b][a] = c
    a, b = sorted([a, b])
    edgelist.append((a, b))
edgelist = set(edgelist)

shortest_edges = set()
for i in range(1, N + 1):
    d, prev = dijkstra(G, i)
    for j in range(1, N + 1):
        if j == i:
            continue
        a, b = sorted([j, prev[j]])
        shortest_edges.add((a, b))

diff = edgelist.difference(shortest_edges)
print(len(diff))
