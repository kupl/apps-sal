import itertools
import networkx as nx
H, W = [int(_) for _ in input().split()]
A = [input() for _ in range(H)]

graph = nx.DiGraph()
for h, w in itertools.product(list(range(H)), list(range(W))):
    if A[h][w] == 'S':
        s = (h, w)
        graph.add_edge(s, (h, -1), capacity=10**10)
        graph.add_edge(s, (-1, w), capacity=10**10)
    elif A[h][w] == 'T':
        t = (h, w)
        graph.add_edge((h, -1), t, capacity=10**10)
        graph.add_edge((-1, w), t, capacity=10**10)
    elif A[h][w] == 'o':
        graph.add_edge((h, -1), (-1, w), capacity=1)
        graph.add_edge((-1, w), (h, -1), capacity=1)
ans = nx.minimum_cut_value(graph, s, t)
print((-1 if ans >= 10**10 else ans))

