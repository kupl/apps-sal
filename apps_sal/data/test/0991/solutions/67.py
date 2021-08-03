from heapq import heappop, heappush
INF = float('inf')

N, M, S = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    U, V, A, B = map(int, input().split())
    graph[U - 1].append((V - 1, A, B))
    graph[V - 1].append((U - 1, A, B))

C, D = [0] * N, [0] * N
for i in range(N):
    c, d = map(int, input().split())
    C[i], D[i] = c, d


def Extdijkstra(start):
    nonlocal S
    N_d = len(graph)
    M = 2500

    if S >= M:
        S = M - 1

    dist = [[INF] * M for _ in range(N_d)]
    dist[start][S] = 0
    q = [(0, S, start)]

    while q:
        d, num, v = heappop(q)
        if num + C[v] < M and d + D[v] < dist[v][num + C[v]]:  # 自己ループ
            dist[v][num + C[v]] = d + D[v]
            heappush(q, (d + D[v], num + C[v], v))
        for node, c, t in graph[v]:
            if num >= c and d + t < dist[node][num - c]:
                dist[node][num - c] = d + t
                heappush(q, (d + t, num - c, node))
    return dist


d = Extdijkstra(0)
for i in range(1, N):
    print(min(d[i]))
