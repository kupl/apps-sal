import numpy as np
h, w = list(map(int, input().split()))
arr = np.array([list(input()) for _ in range(h)]) == "."
# print(arr)
l = np.zeros((h, w), dtype=int)
r = np.zeros((h, w), dtype=int)
u = np.zeros((h, w), dtype=int)
d = np.zeros((h, w), dtype=int)

for i in range(h):
    u[i] = (u[i - 1] + 1) * arr[i] #arrがFalseだと0になる
    d[- i - 1] = (d[- i] + 1) * arr[- i - 1]

for j in range(w):
    l[:, j] = (l[:, j-1] + 1) * arr[:, j]
    r[:, - j - 1] = (r[:, - j] + 1) * arr[:, - j - 1]
# print(u)
print((np.max(u + d + l + r) - 3))

