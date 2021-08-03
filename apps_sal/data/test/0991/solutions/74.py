from scipy.sparse import*
(n, m, s, *D), *t = [map(int, t.split())for t in open(0)]
x = 51
r = range(0, x**3, x)
for u, v, a, b in t[:m]:
    for i in r:
        D += i + a * x + u, i + v, b, i + a * x + v, i + u, b
i = 0
for c, d in t[m:]:
    i += 1
    for j in r:
        D += j + i, j + c * x + i, d
d = csgraph.dijkstra(csr_matrix((D[2::3], (D[::3], D[1::3])), [j * 2] * 2), 1, min(j, s * x) + 1)
for i in range(2, n + 1):
    print(int(min(d[i::x])))
