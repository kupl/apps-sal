
import numpy as np

H, W = list(map(int, input().split()))
M = [list(input()) for _ in range(H)]
M = (np.array(M) == '.') * 1

L = np.zeros((H, W), dtype=int)
R = np.zeros((H, W), dtype=int)
D = np.zeros((H, W), dtype=int)
U = np.zeros((H, W), dtype=int)

for i in range(W):
    if i == 0:
        L[:, i] = M[:, i]
        R[:, W - i - 1] = M[:, W - i - 1]
    else:
        L[:, i] = (L[:, i - 1] + 1) * M[:, i]
        R[:, W - i - 1] = (R[:, W - i] + 1) * M[:, W - i - 1]

for i in range(H):
    if i == 0:
        U[i, :] = M[i, :]
        D[H - i - 1, :] = M[H - i - 1, :]
    else:
        U[i, :] = (U[i - 1, :] + 1) * M[i, :]
        D[H - i - 1, :] = (D[H - i, :] + 1) * M[H - i - 1, :]

print((max(np.max(L + R + D + U - 3), 0)))
