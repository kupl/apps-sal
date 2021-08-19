import numpy as np
(H, W) = map(int, input().split())
S = np.array([list(input().rstrip('\n')) for _ in range(H)]) == '.'
D = np.zeros((H, W), dtype=int)
U = np.zeros((H, W), dtype=int)
L = np.zeros((H, W), dtype=int)
R = np.zeros((H, W), dtype=int)
for i in range(H):
    U[i] = (U[i - 1] + 1) * S[i]
    D[-i - 1] = (D[-i] + 1) * S[-i - 1]
for i in range(W):
    L[:, i] = (L[:, i - 1] + 1) * S[:, i]
    R[:, -i - 1] = (R[:, -i] + 1) * S[:, -i - 1]
print(np.max(U + D + L + R) - 3)
