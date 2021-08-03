from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall
import numpy as np
N = int(input())
A = np.array([list(map(int, input().split())) for _ in [0] * N], dtype=np.int)
D = csgraph_from_dense(A)
D = floyd_warshall(D, directed=False)

if (A == D).all():
    ans = 0
    D += np.identity(N, int) * (1 << 60)
    for i in range(N):
        for j in range(i + 1, N):
            a = np.min(D[i] + D[j])
            if a > D[i, j]:
                ans += D[i, j]
    print((int(ans)))
else:
    print((-1))
