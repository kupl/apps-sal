import networkx as nx
N, M = map(int, input().split())


G = nx.Graph()

for i in range(1, N + 1):
    G.add_node(i)

for i in range(0, M):
    A, B, C = map(int, input().split())
    G.add_edge(A, B)

print(nx.number_connected_components(G))
