#!/usr/bin/env python3
# -*- coding: utf-8 -*-


n = int(input())
X = []
H = []

for i in range(n):
    (x, h) = (int(i) for i in input().split())
    X += [x]
    H += [h]

if n < 3:
    tr = n
else:
    tr = 2
    min = X[0]
    for i in range(1, n - 1):
        if min < X[i] - H[i]:
            tr += 1
            min = X[i]
        elif X[i + 1] > X[i] + H[i]:
            tr += 1
            min = X[i] + H[i]
        else:
            min = X[i]

print(tr)
