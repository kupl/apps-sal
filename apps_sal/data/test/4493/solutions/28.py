# -*- coding: utf-8 -*-

c = [list(map(int, input().split())) for _ in range(3)]

a = [0] * 3
b = [0] * 3

for j in range(3):
    b[j] = c[0][j] - a[0]

for i in range(1, 3, 1):
    a[i] = c[i][0] - b[0]

for i in range(3):
    for j in range(3):
        if c[i][j] != a[i] + b[j]:
            print("No")
            return

print("Yes")
