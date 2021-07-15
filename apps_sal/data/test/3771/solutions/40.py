import networkx as nx

G = nx.Graph()

h, w = map(int, input().split())
grid = [input() for _ in range(h)]
G.add_nodes_from(range(h + w + 2))

for i in range(h):
    for j in range(w):
        if grid[i][j] == "S":
            s = h + w
            G.add_edge(s, i)
            G.add_edge(s, j + h)
        elif grid[i][j] == "T":
            t = h + w + 1
            G.add_edge(i, t)
            G.add_edge(j + h, t)
        elif grid[i][j] == "o":
            G.add_edge(i, j + h, capacity = 1)
            G.add_edge(j + h, i, capacity = 1)

try:
    ans, _ = nx.maximum_flow(G, s, t)
except:
    ans = -1
print(ans)
