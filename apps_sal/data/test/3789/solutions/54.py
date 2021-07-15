import networkx as nx
from  networkx.algorithms.flow import dinitz

n = int(input())
A = list(map(int, input().split()))
G = nx.DiGraph()

source = "source"
sink = "sink"

for i in range(1, n + 1):
    if A[i - 1] <= 0:
        G.add_edge(source, i, capacity=-A[i - 1])
    else:
        G.add_edge(i, sink, capacity=A[i - 1])

for i in range(1, n // 2 + 1):
    for j in range(2 * i, n + 1, i):
        G.add_edge(i, j)

try:
    # mincut = nx.minimum_cut_value(G, source, sink)
    R = dinitz(G, source, sink)
    # print(R, R.graph)
    res = sum(a for a in A if a > 0)
    # print(res - mincut)
    print((res - R.graph["flow_value"]))

except nx.NetworkXError:
    print((0))

