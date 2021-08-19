import numpy as np
h, w = map(int, input().split())
ar = np.array([list(input()) for _ in range(h)]) == '.'
# print(ar)
l = np.zeros((h, w), dtype=int)
r = np.zeros((h, w), dtype=int)
u = np.zeros((h, w), dtype=int)
d = np.zeros((h, w), dtype=int)

for i in range(h):
    u[i] = (u[i - 1] + 1) * ar[i]
    # print(u)
    d[-i - 1] = (d[-i] + 1) * ar[-i - 1]
    # print(d)

for j in range(w):
    l[:, j] = (l[:, j - 1] + 1) * ar[:, j]
    # print(l)
    r[:, -j - 1] = (r[:, -j] + 1) * ar[:, -j - 1]
    # print(r)
print(np.max(u + d + l + r) - 3)
