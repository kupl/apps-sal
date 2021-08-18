
from heapq import heappop, heappush

INF = float("inf")


def dijkstra(n, G, s):
    dist = [INF] * n
    dist[s] = 0
    hq = [(0, s)]
    while hq:
        d, v = heappop(hq)
        if dist[v] < d:
            continue
        for child, child_d in G[v]:
            if dist[child] > dist[v] + child_d:
                dist[child] = dist[v] + child_d
                heappush(hq, (dist[child], child))
    return dist


n, u, v = list(map(int, input().split()))
graph = [[] for _ in range(n)]

edge = [list(map(int, input().split())) for _ in range(n - 1)]

for a, b in edge:
    graph[a - 1].append((b - 1, 1))
    graph[b - 1].append((a - 1, 1))

from_u = dijkstra(n, graph, u - 1)
from_v = dijkstra(n, graph, v - 1)


fil = [x for x in [[fu, fv] for fu, fv in zip(from_u, from_v)] if x[0] < x[1]]
sfil = sorted(list(fil), key=lambda x: [-x[1], -x[0]])


print((sfil[0][1] - 1))
