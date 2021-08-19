from collections import defaultdict
from heapq import heappop, heappush


class Graph(object):
    """
    隣接リストによる有向グラフ
    """

    def __init__(self):
        self.graph = defaultdict(list)

    def __len__(self):
        return len(self.graph)

    def add_edge(self, src, dst, weight=1):
        self.graph[src].append((dst, weight))

    def get_nodes(self):
        return list(self.graph.keys())


class Dijkstra(object):
    """
    ダイクストラ法（二分ヒープ）による最短経路探索
    計算量: O((E+V)logV)
    """

    def __init__(self, graph, start):
        self.g = graph.graph
        self.dist = defaultdict(lambda: float('inf'))
        self.dist[start] = 0
        self.prev = defaultdict(lambda: None)
        self.Q = []
        heappush(self.Q, (self.dist[start], start))
        while self.Q:
            (dist_u, u) = heappop(self.Q)
            if self.dist[u] < dist_u:
                continue
            for (v, weight) in self.g[u]:
                alt = dist_u + weight
                if self.dist[v] > alt:
                    self.dist[v] = alt
                    self.prev[v] = u
                    heappush(self.Q, (alt, v))

    def shortest_distance(self, goal):
        """
        startノードからgoalノードまでの最短距離
        """
        return self.dist[goal]

    def shortest_path(self, goal):
        """
        startノードからgoalノードまでの最短経路
        """
        path = []
        node = goal
        while node is not None:
            path.append(node)
            node = self.prev[node]
        return path[::-1]


g = Graph()
N = int(input())
for i in range(N):
    g.add_edge(i, (i + 1) % N, 1)
    g.add_edge(i, 10 * i % N, 0)
d = Dijkstra(g, 1)
print(d.dist[0] + 1)
