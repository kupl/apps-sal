import networkx as nx

N, M = map(int, input().split())
G = nx.Graph()
G.add_nodes_from(range(1, N + 1))
G.add_edges_from([tuple(map(int, input().split())) for _ in range(M)])

print(len(tuple(nx.bridges(G))))
