import heapq


def dijkstra(G, s, dist):
    dist[s] = 0
    Q = [[0, s]]
    heapq.heapify(Q)
    while len(Q) > 0:
        (cur_d, cur_v) = heapq.heappop(Q)
        cur_d *= -1
        if cur_d > dist[cur_v]:
            continue
        for e in G[cur_v]:
            (to, cost) = (e[0], e[1])
            if dist[cur_v] + cost < dist[to]:
                dist[to] = dist[cur_v] + cost
                heapq.heappush(Q, [-dist[to], to])


N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    (u, v, w) = list(map(int, input().split()))
    (u, v) = (u - 1, v - 1)
    G[u].append([v, w])
    G[v].append([u, w])
dist = [1e+18] * N
dijkstra(G, 0, dist)
for d in dist:
    if d % 2 == 0:
        print(0)
    if d % 2 == 1:
        print(1)
