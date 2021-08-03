# (6,6)周期
# 36種の希望

import numpy as np
N, K = list(map(int, input().split()))
KK = 2 * K
hope = np.zeros((KK, KK), dtype=np.int32)

for _ in range(N):
    x, y, c = input().split()
    x = int(x)
    y = int(y)
    if c == 'B':
        x -= K
    hope[x % KK, y % KK] += 1
# (x,y)を希望された場合、[x,x+K), [y,y+K)に終点があるべき
# 区間の重なってる枚数を集計。1,0,0,-1, cumsum
A = np.zeros((KK + K, KK + K), dtype=np.int32)
A[:-K, :-K] = hope[:]
A[K:, :-K] += -hope[:]
A[:-K, K:] += -hope[:]
A[K:, K:] += hope[:]
A = A.cumsum(axis=0).cumsum(axis=1)

# 実質同じ場所をまとめる
B = A[:, :KK]
B[:, :K] += A[:, KK:]  # (3K,2K)
A = B[:KK, :]
A[:K, :] += B[KK:, :]  # (2K,2K)
B = A[:K, :]  # (K,2K)
B[:, :K] += A[K:, K:]
B[:, K:] += A[K:, :K]

answer = B.max()
print(answer)
