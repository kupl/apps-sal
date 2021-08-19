from numpy import *
from scipy.sparse.csgraph import *
(H, W) = map(int, input().split())
G = array([list(map(int, input().split())) for n in range(10)])
A = [list(map(int, input().split())) for h in range(H)]
F = shortest_path(G)
ans = 0
for h in range(H):
    for w in range(W):
        if A[h][w] != -1:
            ans += F[A[h][w]][1]
print(int(ans))
