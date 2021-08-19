from heapq import heapify, heappush, heappop
N = int(input())
abclist = [list(map(int, input().split())) for _ in range(N - 1)]
(Q, K) = map(int, input().split())
xylist = [list(map(int, input().split())) for _ in range(Q)]
inf = float('inf')


def dijkstra(graph, start):
    vsize = len(graph)
    dist = [inf] * vsize
    seen = [False] * vsize
    prev = [None] * vsize
    pq = []
    heapify(pq)
    dist[start] = 0
    heappush(pq, (0, start))
    while pq:
        (cost, u) = heappop(pq)
        seen[u] = True
        if dist[u] < cost:
            continue
        for (v, w) in graph[u]:
            temp_cost = dist[u] + w
            if not seen[v] and temp_cost < dist[v]:
                dist[v] = temp_cost
                prev[v] = u
                heappush(pq, (dist[v], v))
    return (dist, prev)


graph = [[] for _ in range(N)]
for (a, b, c) in abclist:
    graph[a - 1].append((b - 1, c))
    graph[b - 1].append((a - 1, c))
(shortest_paths, prev) = dijkstra(graph, K - 1)
for (x, y) in xylist:
    print(shortest_paths[x - 1] + shortest_paths[y - 1])
