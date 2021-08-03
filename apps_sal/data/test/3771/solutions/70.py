import networkx as nx

H, W = map(int, input().split())
a = [input() for _ in range(H)]
INF = 10**20

G = nx.Graph()
G.add_nodes_from(range(0, H + W + 2))
for i in range(H):
    for j in range(W):
        if a[i][j] == 'o':
            G.add_edge(i + 1, j + H + 1, capacity=1)
        if a[i][j] == 'S':
            G.add_edge(0, i + 1, capacity=INF)
            G.add_edge(0, j + H + 1, capacity=INF)
        if a[i][j] == 'T':
            G.add_edge(H + W + 1, i + 1, capacity=INF)
            G.add_edge(H + W + 1, j + H + 1, capacity=INF)

flow_value, flow_dict = nx.maximum_flow(G, 0, H + W + 1)
print(flow_value if flow_value < INF else -1)
