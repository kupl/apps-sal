#! /usr/bin/env python
# -*- coding: utf-8 -*-

n, h = list(map(int, input().split()))
xs = [list(map(int, input().split())) for _ in range(n)]

s = [i for i, _ in xs]
t = [i for _, i in xs]

L = 0
R = 0
ans = 0

while L < n:
    while (R < n - 1) and (h - (s[R + 1] - t[R])) > 0:
        h -= s[R + 1] - t[R]
        R += 1
    if t[R] - s[L] + h > ans:
        ans = t[R] - s[L] + h

    if L < n - 1:
        h += s[L + 1] - t[L]
    L += 1
print(ans)
