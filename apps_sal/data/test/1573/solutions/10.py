#!/usr/bin/env python
# -*- coding: utf-8 -*-

n, d = list(map(int, input().split()))
F = []
for i in range(n):
    F.append(list(map(int, input().split())))

F = sorted(F, key=lambda x: x[0])
f_factor = 0
j = 0
ans = -1
for i in range(n):
    if i != 0:
        f_factor -= F[i - 1][1]
    while j < n:
        if F[j][0] - F[i][0] >= d:
            break
        f_factor += F[j][1]
        j += 1
    ans = max(ans, f_factor)
print(ans)
