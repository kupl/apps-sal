import collections
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall
(H, W, *S) = open(0).read().split()
(H, W) = [int(_) for _ in [H, W]]
A = []
B = []
C = []
for i in range(H * W):
    (x, y) = divmod(i, W)
    if S[x][y] == '.':
        for (dx, dy) in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            (nx, ny) = (x + dx, y + dy)
            if not (0 <= nx < H and 0 <= ny < W):
                continue
            if S[nx][ny] == '.':
                A += [i]
                B += [nx * W + ny]
                C += [1]
F = floyd_warshall(csr_matrix((C, (A, B)), shape=(H * W, H * W)))
print(int(np.max(F[F != np.inf])))
