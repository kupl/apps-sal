import numpy as np
(H, W) = list(map(int, input().split()))
field = [[c == '.' for c in input()] for _ in range(H)]
field = np.array(field, dtype=np.int16)
u = field.copy()
d = field.copy()
l = field.copy()
r = field.copy()
for i in range(1, H):
    u[i] = (u[i - 1] + 1) * u[i]
    d[-i - 1] = (d[-i] + 1) * d[-i - 1]
for j in range(1, W):
    l[:, j] = (l[:, j - 1] + 1) * l[:, j]
    r[:, -j - 1] = (r[:, -j] + 1) * r[:, -j - 1]
print((u + d + l + r - 3).max())
