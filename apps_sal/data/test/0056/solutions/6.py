import sys
import math
res = [0]
(n, m) = map(int, input().split())
z = []
need = 0
for i in range(1, n + 1):
    need += i
for i in range(1, n + 1):
    z.append([0] * i)
for i in range(1, m + 1):
    z[0][0] += 2
    for i in range(n - 1):
        for j in range(i + 1):
            if z[i][j] >= 2:
                h = z[i][j] - 2
                z[i + 1][j] += h / 2
                z[i + 1][j + 1] += h / 2
                z[i][j] = 2
    for j in range(n):
        if z[-1][j] >= 2:
            z[-1][j] = 2
s = 0
for i in range(n):
    s += z[i].count(2)
print(s)
