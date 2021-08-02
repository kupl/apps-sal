from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix
from itertools import permutations

N, M, R = list(map(int, input().split()))
r = list(map(int, input().split()))
abc = [list(map(int, input().split())) for _ in range(M)]

r = [e - 1 for e in r]

g = [[0] * N for _ in range(N)]
for a, b, c in abc:
    a -= 1
    b -= 1
    g[a][b] = c
    g[b][a] = c

dist = floyd_warshall(csr_matrix(g))

ans = float("inf")
for pat in permutations(r, len(r)):
    sm = 0
    for e1, e2 in zip(pat, pat[1:]):
        sm += dist[e1][e2]

    ans = min(ans, sm)

ans = int(ans)
print(ans)
