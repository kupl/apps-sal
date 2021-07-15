import networkx as nx

n, m, *AB = map(int, open(0).read().split())
G = nx.Graph()
G.add_edges_from(zip(AB[::2], AB[1::2]))
print(len(list(nx.bridges(G))))
