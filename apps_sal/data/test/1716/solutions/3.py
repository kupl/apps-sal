import numpy as np
(N, M, Q) = map(int, input().split())
table = np.zeros((N, N), np.int64)
for _ in range(M):
    (L, R) = map(lambda n: int(n) - 1, input().split())
    table[L][R] += 1
table = np.rot90(np.rot90(table, k=-1).cumsum(axis=0).cumsum(axis=1), k=1)
for _ in range(Q):
    (p, q) = map(lambda n: int(n) - 1, input().split())
    print(table[p][q])
