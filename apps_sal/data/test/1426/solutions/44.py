import heapq
INF = 10 ** 10


def dijkstra(n, adj, s, t):
    dist = [INF for _ in range(n)]
    dist[s] = 0
    h = [(0, s)]
    while len(h) > 0:
        d, node = heapq.heappop(h)
        for next_node in adj[node]:
            next_d = d + 1
            if next_d < dist[next_node]:
                dist[next_node] = next_d
                heapq.heappush(h, (next_d, next_node))
    return dist[t]


def main():
    N, M = list(map(int, input().split(' ')))
    adj = [[] for _ in range(3 * N)]
    for _ in range(M):
        u, v = list(map(lambda x: int(x) - 1, input().split(' ')))
        adj[3 * u].append(3 * v + 1)
        adj[3 * u + 1].append(3 * v + 2)
        adj[3 * u + 2].append(3 * v)
    S, T = list(map(lambda x: int(x) - 1, input().split(' ')))
    d = dijkstra(3 * N, adj, 3 * S, 3 * T)
    if d == INF:
        print(-1)
    else:
        print(d // 3)


def __starting_point():
    main()
__starting_point()
