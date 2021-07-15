import numpy as np

H, W = list(map(int, input().split(' ')))

S = np.array([[int(c == '.') for c in input()] for _ in range(H)])

up = S.copy()
down = S.copy()
left = S.copy()
right = S.copy()

for i in range(1, H):
    up[i] = (up[i - 1] + 1) * up[i]
    down[-i - 1] = (down[-i] + 1) * down[-i - 1]

for i in range(1, W):
    left[:, i] = (left[:, i - 1] + 1) * left[:, i]
    right[:, -i - 1] = (right[:, -i] + 1) * right[:, -i - 1]

print((np.max(up + down + left + right) - 3))

