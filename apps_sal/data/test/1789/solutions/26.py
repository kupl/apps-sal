import collections
import heapq


class Dijkstra:
    def __init__(self):
        self.e = collections.defaultdict(list)

    def add(self, u, v, d):
        self.e[u].append([v, d])
        self.e[v].append([u, d])

    def delete(self, u, v):
        self.e[u] = [_ for _ in self.e[u] if _[0] != v]
        self.e[v] = [_ for _ in self.e[v] if _[0] != u]

    def search(self, s):
        """
        :param s: 始点
        :return: 始点から各点までの最短経路
        """
        d = collections.defaultdict(lambda: float('inf'))
        d[s] = 0
        q = []
        heapq.heappush(q, (0, s))
        v = collections.defaultdict(bool)
        while len(q):
            k, u = heapq.heappop(q)
            if v[u]:
                continue
            v[u] = True

            for uv, ud in self.e[u]:
                if v[uv]:
                    continue
                vd = k + ud
                if d[uv] > vd:
                    d[uv] = vd
                    heapq.heappush(q, (vd, uv))

        return d

A,B,X,Y = map(int, input().split())
graph = Dijkstra()
for i in range(1,101):
    graph.add(i,100+i,X)
for i in range(1,100):
    graph.add(i+1,100+i,X)
for i in range(1,100):
    graph.add(i,i+1,Y)
    graph.add(100+i,100+i+1,Y)
SA = graph.search(A)
print(SA[B+100])
