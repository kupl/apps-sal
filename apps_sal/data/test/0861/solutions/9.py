#!/usr/bin/env python3
from math import sqrt
m, r = list(map(int, input().split()))
acc = 0.0
for i in range(m):
    acc += 2 * r
    for j in [i, m - i - 1]:
        if j:
            acc += (2 + sqrt(2)) * r
            acc += (2 * (j - 1) * j / 2 + 2 * sqrt(2) * (j - 1)) * r
print('%.12f' % (acc / (m**2)))
