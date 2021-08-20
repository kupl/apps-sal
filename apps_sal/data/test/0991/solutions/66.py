from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix
(N, M, S, *I) = map(int, open(0).read().split())
(UVAB, CD) = (I[:4 * M], I[4 * M:])
(R, C, V) = ([], [], [])
for (u, v, a, b) in zip(*[iter(UVAB)] * 4):
    for i in range(2501 - a):
        R += [(i + a) * 51 + u, (i + a) * 51 + v]
        C += [i * 51 + v, i * 51 + u]
        V += [b, b]
for (i, (c, d)) in enumerate(zip(*[iter(CD)] * 2), 1):
    for j in range(2501 - c):
        R.append(j * 51 + i)
        C.append((j + c) * 51 + i)
        V.append(d)
D = dijkstra(csr_matrix((V, (R, C)), [2500 * 60] * 2), indices=min(2500, S) * 51 + 1)
for i in range(2, N + 1):
    print(int(D[i::51].min()))
