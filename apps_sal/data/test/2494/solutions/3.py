from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra


class Graph(object):

    def __init__(self, K):
        self.K = K
        self.weights = {}

    def add(self, node1, node2, weight):
        if (node1, node2) in self.weights:
            self.weights[node1, node2] = min(self.weights[node1, node2], weight)
        else:
            self.weights[node1, node2] = weight

    def to_csr(self):
        (n1, n2, w) = ([], [], [])
        for ((node1, node2), weight) in self.weights.items():
            n1.append(node1)
            n2.append(node2)
            w.append(weight)
        return csr_matrix((w, (n1, n2)), shape=(self.K, self.K))


K = int(input())
g = Graph(K)
for i in range(K):
    if i == K - 1:
        g.add(i, 0, 1)
    else:
        g.add(i, i + 1, 1)
    g.add(i, i * 10 % K, 10 ** (-8))
d = dijkstra(g.to_csr(), directed=True, indices=1)
print(int(d[0]) + 1)
