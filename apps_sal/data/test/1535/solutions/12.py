from math import *
(n, x0, y0) = list(map(int, input().split()))
a = []
for i in range(n):
    (x, y) = list(map(int, input().split()))
    a.append([x, y])
cnt = 0
for i in range(n):
    if a[i] == -1:
        continue
    A = a[i][1] - y0
    B = x0 - a[i][0]
    C = -x0 * A + y0 * (a[i][0] - x0)
    for j in range(n):
        if a[j] == -1:
            continue
        if A * a[j][0] + B * a[j][1] + C == 0:
            a[j] = -1
    cnt += 1
print(cnt)
