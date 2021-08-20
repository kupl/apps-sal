from math import sqrt
n = int(input())
m = {}
for i in range(n):
    line = input()
    mi = [int(x) for x in line.strip().split()]
    for j in range(n):
        if i not in m:
            m[i] = {}
        m[i][j] = mi[j]
res = []
for i in range(n):
    x = m[i][(i + 1) % n]
    y = m[i][(i + 2) % n]
    z = m[(i + 1) % n][(i + 2) % n]
    res.append(str(int(sqrt(int(x * y / z)))))
print(' '.join(res))
