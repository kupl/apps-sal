from itertools import chain
import numpy as np
import networkx as nx
X = iter(open(0).readlines())
(h, w) = map(int, next(X).split())
C = np.zeros((10, 10), dtype=int)
for i in range(10):
    for (j, c) in enumerate(map(int, next(X).split())):
        C[i, j] = c
A = np.zeros((h, w), dtype=int)
for i in range(h):
    for (j, a) in enumerate(map(int, next(X).split())):
        A[i, j] = a
G = nx.DiGraph(C)
d = {}
for i in range(10):
    if i == 1:
        continue
    d[i] = nx.shortest_path_length(G, i, 1, weight='weight')
s = 0
for a in chain.from_iterable(A):
    if a == -1 or a == 1:
        continue
    s += d[a]
print(s)
