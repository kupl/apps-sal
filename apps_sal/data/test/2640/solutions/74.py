import numpy as np
H, W = map(int, input().split())
l = np.zeros((H, W), dtype=int)
r = np.zeros((H, W), dtype=int)
d = np.zeros((H, W), dtype=int)
u = np.zeros((H, W), dtype=int)
s = np.array([list(input()) for _ in range(H)]) == "."
for i in range(H):
    u[i] = (u[i - 1] + 1) * s[i]
    d[-i - 1] = (d[-i] + 1) * s[-i - 1]
for i in range(W):
    l[:, i] = (l[:, i - 1] + 1) * s[:, i]
    r[:, -i - 1] = (r[:, -i] + 1) * s[:, -i - 1]
print(np.max(u + d + l + r) - 3)
