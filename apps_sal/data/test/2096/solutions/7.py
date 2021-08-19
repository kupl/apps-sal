#!/usr/bin/env python3
n = int(input())
a = list(map(int, input().split()))
c = [0] * 100
for i in a:
    c[i] += 1
x = [0] * 100
y = [0] * 100
j = 0
for i in range(100):
    if c[i] == 1:
        [x, y][j][i] += 1
        j = 1 - j
for i in range(100):
    if c[i] != 1:
        x[i] += c[i] // 2
        y[i] += c[i] // 2
        if c[i] % 2 == 1:
            [x, y][j][i] += 1
            j = 1 - j
xk = len(list([it for it in x if it]))
yk = len(list([it for it in y if it]))
print(xk * yk)
zs = [None] * (2 * n)
for i in range(2 * n):
    if x[a[i]] > 0:
        x[a[i]] -= 1
        zs[i] = 1
    else:
        assert y[a[i]] > 0
        y[a[i]] -= 1
        zs[i] = 2
print(*zs)
