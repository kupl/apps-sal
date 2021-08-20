import numpy as np
(h, w) = list(map(int, input().split()))
s = np.array([list(input()) for _ in range(h)]) == '.'
L = np.zeros((h, w), dtype=int)
R = np.zeros((h, w), dtype=int)
U = np.zeros((h, w), dtype=int)
D = np.zeros((h, w), dtype=int)
for i in range(h):
    D[i] = (D[i - 1] + 1) * s[i]
    U[-i - 1] = (U[-i] + 1) * s[-i - 1]
for i in range(w):
    R[:, i] = (R[:, i - 1] + 1) * s[:, i]
    L[:, -i - 1] = (L[:, -i] + 1) * s[:, -i - 1]
print(np.max(D + U + R + L) - 3)
