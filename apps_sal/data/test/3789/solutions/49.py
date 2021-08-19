import networkx as nx

n = int(input())
A = list(map(int, input().split()))
G = nx.DiGraph()

source = "source"
sink = "sink"

for i in range(1, n + 1):
    x, y = A[i - 1], 0
    if A[i - 1] < 0:
        x, y = y, -x
    G.add_edge(source, i, capacity=x)
    G.add_edge(i, sink, capacity=y)

for i in range(1, n // 2 + 1):
    for j in range(2 * i, n + 1, i):
        # print(i, j)
        G.add_edge(j, i)

try:
    mincut, cut_dic = nx.minimum_cut(G, source, sink)
    res = sum(a for a in A if a > 0)
    print((res - mincut))


except nx.NetworkXError:
    print((0))
