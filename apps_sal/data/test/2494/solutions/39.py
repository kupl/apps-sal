from scipy.sparse.csgraph import dijkstra, shortest_path
from scipy.sparse import csr_matrix
K = int(input())


class Graph(object):

    def __init__(self, K):
        self.K = K
        self.weights = {}

    def add_edge(self, node1, node2, weight):
        if (node1, node2) in self.weights:
            self.weights[(node1, node2)] = min(self.weights[(node1, node2)], weight)
        else:
            self.weights[(node1, node2)] = weight

    def get_csr_matrix(self):
        n1, n2, w = [], [], []
        for (node1, node2), weight in self.weights.items():
            n1.append(node1)
            n2.append(node2)
            w.append(weight)
        return csr_matrix((w, (n1, n2)), shape=(self.K, self.K))


g = Graph(K)

for i in range(K - 1):
    g.add_edge(i, i + 1, 1)
    g.add_edge(i, (i * 10) % K, 10**(-16))

g.add_edge(K - 1, 0, 1)
g.add_edge(K - 1, ((K - 1) * 10) % K, 10**(-16))
d = dijkstra(g.get_csr_matrix(), directed=True, indices=1)
print(int(d[0]) + 1)
