import networkx as nx
N = int(input())
ab = [list(map(int, input().split())) for _ in range(N)]
ab = sorted(ab)
cd = [list(map(int, input().split())) for _ in range(N)]
cd = sorted(cd, reverse=True)
G = nx.DiGraph()
for i in range(N):
    G.add_edge('x', i, capacity=1)
    for j in range(N):
        if i == 0:
            G.add_edge(N + j, 'y', capacity=1)
        (a, b) = ab[i]
        (c, d) = cd[j]
        if a < c and b < d:
            G.add_edge(i, N + j, capacity=1)
        elif a >= c:
            break
(flow_value, flow_dict) = nx.maximum_flow(G, 'x', 'y')
print(flow_value)
