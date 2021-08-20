from itertools import chain
import numpy as np
import networkx as nx
(h, w, *X) = map(int, open(0).read().split())
C = np.array(X[:100], dtype=int).reshape((10, 10)).T
A = np.array(X[100:], dtype=int).reshape((h, w))
G = nx.DiGraph(C)
d = {-1: 0}
d.update(nx.single_source_dijkstra_path_length(G, 1, weight='weight'))
print(sum((d[a] for a in chain(*A))))
