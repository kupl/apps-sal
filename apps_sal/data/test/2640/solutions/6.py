import numpy as np
H, W = map(int, input().split())
S = np.zeros((H, W))
for i in range(H):
    Si = np.array([int(s == '.') for s in input()])
    S[i] = Si

top = S.copy()
bottom = S.copy()
left = S.copy()
right = S.copy()

for i in range(1, H):
    top[i] = (top[i - 1] + 1) * S[i]
    bottom[-i - 1] = (bottom[-i] + 1) * S[-i - 1]

for j in range(1, W):
    left[:, j] = (left[:, j - 1] + 1) * S[:, j]
    right[:, -j - 1] = (right[:, -j] + 1) * S[:, -j - 1]

print(np.max((top + bottom + left + right - 3).astype(np.int)))
