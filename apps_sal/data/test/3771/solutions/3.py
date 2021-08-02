from networkx import*
H, *S = open(0)
H, W = map(int, H.split())
g = Graph()
a = g.add_edges_from
for i in range(m := H * W): a([[M := m * 2, h := i // W], [M, w := i % W + m]] * ((c := S[h][w - m]) == 'S') + [[h, I := m * 3], [w, I]] * (c == 'T'), capacity=I), a([[h, w], [w, h]] * (c > 'T'), capacity=1)
f, _ = minimum_cut(g, M, I)
print(-(f > M) or f)
