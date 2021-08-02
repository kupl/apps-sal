from networkx import*
n, *A = map(int, open(s := 0).read().split())
G = DiGraph()
G.add_nodes_from(range(n + 2))
for i, a in enumerate(A, 1):
    if a > 0:
        s += a
        G.add_edge(i, n + 1, capacity=a)
    else: G.add_edge(0, i, capacity=-a)
    for j in range(i + i, n + 1, i): G.add_edge(i, j, capacity=9e20)
print(s - maximum_flow(G, 0, n + 1)[0])
