import numpy as np
(N, M, Q, *LRpq) = list(map(int, open(0).read().split()))
(LR, pq) = (LRpq[:2 * M], LRpq[2 * M:])
del LRpq
acc = np.zeros((N + 1, N + 1), dtype=np.int64)
for (L, R) in zip(*[iter(LR)] * 2):
    acc[L][R] += 1
acc = np.cumsum(acc, axis=0)
acc = np.cumsum(acc, axis=1)
ans = [0] * Q
for (i, (p, q)) in enumerate(zip(*[iter(pq)] * 2)):
    ans[i] = acc[q][q] + acc[p - 1][p - 1] - acc[p - 1][q] - acc[q][p - 1]
print('\n'.join(map(str, ans)))
