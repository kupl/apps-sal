from scipy.sparse.csgraph import floyd_warshall
from numpy import where
n, m, l = map(int, input().split())
abc = [list(map(int, input().split()))for i in range(m)]
q = int(input())
st = [list(map(int, input().split()))for i in range(q)]
t = [[float("inf")] * n for _ in range(n)]
for a, b, c in abc:
    if c <= l:
        t[a - 1][b - 1] = c
f = floyd_warshall(t, 0)
l = floyd_warshall(where(f <= l, 1, f), 0)
for s, t in st:
    print(-1if l[s - 1, t - 1] == float("inf")else int(l[s - 1, t - 1]) - 1)
