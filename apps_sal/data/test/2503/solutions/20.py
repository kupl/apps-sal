import numpy as np
(N, K) = list(map(int, input().split()))
B = np.zeros((2 * K, 2 * K), np.int32)
for _ in range(N):
    (x, y, c) = input().split()
    if c == 'B':
        B[int(x) % (2 * K)][int(y) % (2 * K)] += 1
    else:
        B[int(x) % (2 * K)][(int(y) + K) % (2 * K)] += 1
SB = np.zeros((4 * K + 1, 4 * K + 1), np.int32)
SB[0 * K + 1:2 * K + 1, 0 * K + 1:2 * K + 1] = B
SB[0 * K + 1:2 * K + 1, 2 * K + 1:4 * K + 1] = B
SB[2 * K + 1:4 * K + 1, 0 * K + 1:2 * K + 1] = B
SB[2 * K + 1:4 * K + 1, 2 * K + 1:4 * K + 1] = B
np.cumsum(SB, 0, out=SB)
np.cumsum(SB, 1, out=SB)
ans = 0
cand = SB[1 * K:3 * K + 1, 1 * K:3 * K + 1].copy()
cand -= SB[0 * K:2 * K + 1, 1 * K:3 * K + 1]
cand -= SB[1 * K:3 * K + 1, 0 * K:2 * K + 1]
cand += SB[0 * K:2 * K + 1, 0 * K:2 * K + 1]
cand += SB[2 * K:4 * K + 1, 2 * K:4 * K + 1]
cand -= SB[1 * K:3 * K + 1, 2 * K:4 * K + 1]
cand -= SB[2 * K:4 * K + 1, 1 * K:3 * K + 1]
cand += SB[1 * K:3 * K + 1, 1 * K:3 * K + 1]
ans = np.max(cand)
print(ans)
