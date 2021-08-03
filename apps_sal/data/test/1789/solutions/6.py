import heapq
a, b, x, y = map(int, input().split())
a, b = a - 1, b - 1
g = [[] for _ in range(200)]
for i in range(100):
    g[i].append((x, 100 + i))
    g[100 + i].append((x, i))
for i in range(99):
    g[i + 1].append((x, 100 + i))
    g[100 + i].append((x, i + 1))
for i in range(99):
    g[i].append((y, i + 1))
    g[i + 1].append((y, i))
for i in range(99):
    g[i + 100].append((y, i + 1 + 100))
    g[i + 1 + 100].append((y, i + 100))

INF = 10**18


def dijkstra_heap(s, edge):
    n = len(edge)
    d = [INF] * n
    used = [True] * n  # True: not used
    d[s] = 0
    used[s] = False
    edgelist = []
    for e in edge[s]:
        heapq.heappush(edgelist, e)
    while len(edgelist):
        minedge = heapq.heappop(edgelist)
        if not used[minedge[1]]:
            continue
        v = minedge[1]
        d[v] = minedge[0]
        used[v] = False
        for e in edge[v]:
            if used[e[1]]:
                heapq.heappush(edgelist, (e[0] + d[v], e[1]))
    return d


d = dijkstra_heap(a, g)
print(d[b + 100])
