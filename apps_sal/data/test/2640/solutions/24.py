# 写経AC
import numpy as np
H, W = list(map(int, input().split()))
L = np.zeros((H, W), int)
R = np.zeros((H, W), int)
D = np.zeros((H, W), int)
U = np.zeros((H, W), int)
S = np.array([list(input()) for h in range(H)]) == "."

for h in range(H):
    U[h] = S[h] * (U[h - 1] + 1)
    D[-h - 1] = S[-h - 1] * (D[-h] + 1)

for w in range(W):
    L[:, w] = S[:, w] * (L[:, w - 1] + 1)
    R[:, -w - 1] = S[:, -w - 1] * (R[:, -w] + 1)

print((np.max(U + D + L + R) - 3))
