import numpy as np


def getBoundary(p, k, k2):
    if p - k + 1 >= 0:
        return [(p - k + 1, p + 1)]
    else:
        return [(0, p + 1), ((p - k + 1) % k2, k2)]


n, k = list(map(int, input().strip().split()))
k2 = k * 2
b = [[0 for i in range(k2 + 1)] for j in range(k2 + 1)]

for i in range(n):
    x_str, y_str, c_str = input().strip().split()
    x = int(x_str) % k2
    y = (int(y_str) + (c_str == 'B') * k) % k2
    for xb, xe in getBoundary(x % k2, k, k2):
        for yb, ye in getBoundary(y % k2, k, k2):
            b[xb][yb] += 1
            b[xb][ye] -= 1
            b[xe][yb] -= 1
            b[xe][ye] += 1
    for xb, xe in getBoundary((x + k) % k2, k, k2):
        for yb, ye in getBoundary((y + k) % k2, k, k2):
            b[xb][yb] += 1
            b[xb][ye] -= 1
            b[xe][yb] -= 1
            b[xe][ye] += 1

arr_b = np.array(b)
for i in range(k2):
    arr_b[i + 1] += arr_b[i]
for j in range(k2):
    arr_b[:, j + 1] += arr_b[:, j]
print((arr_b.max()))
