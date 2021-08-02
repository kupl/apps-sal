import numpy as np
H, W = list(map(int, input().split()))
S = np.array([list(input()) for _ in range(H)])
S = np.where(S == '.', 1, 0)


L = np.zeros((H, W), dtype=np.int)
R = np.zeros((H, W), dtype=np.int)
U = np.zeros((H, W), dtype=np.int)
D = np.zeros((H, W), dtype=np.int)

for i in range(W):
    L[:, i] = (L[:, i - 1] + 1) * S[:, i]
    R[:, -i - 1] = (R[:, -i] + 1) * S[:, -i - 1]
for j in range(H):
    U[j, :] = (U[j - 1, :] + 1) * S[j, :]
    D[-j - 1, :] = (D[-j, :] + 1) * S[-j - 1, :]

print((np.max(L + R + U + D) - 3))
