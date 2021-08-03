import networkx as nx
N = int(input())
AB = [[int(_) for _ in input().split()] for _ in range(N)]
CD = [[int(_) for _ in input().split()] for _ in range(N)]
G = nx.DiGraph()
for a, b in AB:
    G.add_edge(-1, a * 1000 + b, capacity=1)
for c, d in CD:
    G.add_edge(c * 1000 + d, -2, capacity=1)
for a, b in AB:
    for c, d in CD:
        if a < c and b < d:
            G.add_edge(a * 1000 + b, c * 1000 + d, capacity=1)
flow_value, flow_dict = nx.maximum_flow(G, -1, -2)
print(flow_value)
