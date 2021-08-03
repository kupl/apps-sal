import networkx as X
n, m = map(int, input().split())
g = X.Graph()
for i in range(n):
    g.add_node(i + 1)
for i in range(m):
    x, y, z = map(int, input().split())
    g.add_edge(x, y)
print(X.number_connected_components(g))
