from heapq import heappush, heappop


class Dijkstra:

    def __init__(self, N):
        self.N = N
        self.E = [[] for _ in range(N)]

    def add_edge(self, init, end, weight, undirected=False):
        self.E[init].append((end, weight))
        if undirected:
            self.E[end].append((init, weight))

    def distance(self, s):
        INF = float('inf')
        (E, N) = (self.E, self.N)
        self.dist = dist = [INF] * N
        self.prev = prev = [-1] * N
        dist[s] = 0
        n_visited = 1
        heap = []
        heappush(heap, (0, s))
        while heap:
            (d, v) = heappop(heap)
            if dist[v] < d:
                continue
            for (u, c) in E[v]:
                temp = d + c
                if dist[u] > temp:
                    dist[u] = temp
                    prev[u] = v
                    heappush(heap, (temp, u))
            n_visited += 1
            if n_visited == N:
                break
        return dist

    def shortest_path(self, t):
        P = []
        prev = self.prev
        while True:
            P.append(t)
            t = prev[t]
            if t == -1:
                break
        return P[::-1]


(N, M) = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
(S, T) = map(int, input().split())
dijkstra = Dijkstra(3 * N)
for (a, b) in edges:
    (a, b) = (a - 1, b - 1)
    dijkstra.add_edge(a, N + b, 0)
    dijkstra.add_edge(N + a, 2 * N + b, 0)
    dijkstra.add_edge(2 * N + a, b, 1)
ans = dijkstra.distance(S - 1)[T - 1]
print(ans if ans != float('inf') else -1)
