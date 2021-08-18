import numpy as np
h, w = map(int, input().split())
s = [list(input()) for i in range(h)]
li = [[0 if s[i][j] == "
l, r, u, d = np.array(li), np.array(li), np.array(li), np.array(li)
for i in range(1, h):
    u[i] *= (u[i - 1] + 1)
    d[-i - 1] *= (d[-i] + 1)
for i in range(1, w):
    l[:, i] *= (l[:, i - 1] + 1)
    r[:, -i - 1] *= (r[:, -i] + 1)
print((l + r + u + d - 3).max())
