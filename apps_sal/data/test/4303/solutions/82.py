import numpy as np
N, K = list(map(int, input().split()))
X = np.array(input().split(), dtype=np.int64)

INF = 10 ** 18
neg = np.concatenate([-X[X <= 0][::-1], np.full(N + 1, INF, dtype=np.int64)])[:K]
pos = np.concatenate([X[X > 0], np.full(N + 1, INF, dtype=np.int64)])[:K]

answer = INF
answer = min(answer, neg[-1])
answer = min(answer, pos[-1])
if K >= 2:
    answer = min(answer, (neg[:K - 1] * 2 + pos[K - 2::-1]).min())
    answer = min(answer, (pos[:K - 1] * 2 + neg[K - 2::-1]).min())

print(answer)
