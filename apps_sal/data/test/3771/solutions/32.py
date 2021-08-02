from networkx import*
H, W = map(int, input().split())
X = [[a for a in input()] for _ in range(H)]
G = Graph()
G.add_nodes_from(range(-2, H + W))
for i in range(H):
    for j in range(W):
        if X[i][j] == "o":
            G.add_edge(i, j + H, capacity=1)
        elif X[i][j] == "S":
            si, sj = i, j
        elif X[i][j] == "T":
            ti, tj = i, j

G.add_edge(-1, si, capacity=1 << 20)
G.add_edge(-1, sj + H, capacity=1 << 20)
G.add_edge(-2, ti, capacity=1 << 20)
G.add_edge(-2, tj + H, capacity=1 << 20)

mf = maximum_flow(G, -1, -2)[0]
print(-1 if mf > 1 << 19 else mf)
