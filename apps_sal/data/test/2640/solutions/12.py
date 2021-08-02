import numpy as np

H, W = map(int, input().split())
S = np.array([list(input()) for _ in range(H)])
S = np.where(S == ".", 1, 0)

L = np.zeros((H, W), dtype=int)
R = np.zeros((H, W), dtype=int)
D = np.zeros((H, W), dtype=int)
U = np.zeros((H, W), dtype=int)

for i in range(H):
    D[-i - 1] = (D[-i] + 1) * S[-i - 1]
    U[i] = (U[i - 1] + 1) * S[i]

for i in range(W):
    L[:, i] = (L[:, i - 1] + 1) * S[:, i]
    R[:, -i - 1] = (R[:, -i] + 1) * S[:, -i - 1]

print(np.max(L + R + D + U) - 3)
