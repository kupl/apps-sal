import numpy as np
(N, M, Q) = map(int, input().split())
table = [[0] * N for _ in range(N)]
for _ in range(M):
    (L, R) = map(lambda n: int(n) - 1, input().split())
    table[R][-L - 1] += 1
table = np.array(table, dtype=np.int64).cumsum(axis=0).cumsum(axis=1).tolist()
for _ in range(Q):
    (p, q) = map(lambda n: int(n) - 1, input().split())
    print(table[q][-p - 1])
