import heapq
k = int(input())
INF = 10 ** 9


class Dijkstra:

    def __init__(self, adj):
        self.adj = adj
        self.num = len(adj)
        self.dist = [INF] * self.num
        self.prev = [INF] * self.num
        self.q = []

    def calc(self, start):
        self.dist[start] = 0
        heapq.heappush(self.q, (0, start))
        while len(self.q) != 0:
            (prov_cost, src) = heapq.heappop(self.q)
            if self.dist[src] < prov_cost:
                continue
            for (dest, cost) in self.adj[src]:
                if self.dist[dest] > self.dist[src] + cost:
                    self.dist[dest] = self.dist[src] + cost
                    heapq.heappush(self.q, (self.dist[dest], dest))
                    self.prev[dest] = src
        return self.dist


edge = [[] for _ in range(k)]
for i in range(k):
    edge[i].append([(i + 1) % k, 1])
    edge[i].append([i * 10 % k, 0])
DIJ = Dijkstra(edge)
DIJ.calc
print(DIJ.calc(1)[0] + 1)
