import networkx as nx
N = int(input())
ABs = [tuple(map(int, input().split())) for _ in range(N)]
CDs = [tuple(map(int, input().split())) for _ in range(N)]
DG = nx.DiGraph()
DG.add_nodes_from(list(range(2 * N + 3)))
for i in range(N):
    for j in range(N):
        if ABs[i][0] < CDs[j][0] and ABs[i][1] < CDs[j][1]:
            DG.add_edge(i, j + N, capacity=1)
DG.add_edges_from([(2 * N + 1, i, {'capacity': 1}) for i in range(N)])
DG.add_edges_from([(i, 2 * N + 2, {'capacity': 1}) for i in range(N, 2 * N)])
print(nx.maximum_flow_value(DG, 2 * N + 1, 2 * N + 2))
