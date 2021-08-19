#!/usr/bin/env python3
n, m = list(map(int, input().split()))
d = m
r = d + 1
for i in range(m):
    if d <= 0:
        break
    a = i + 1
    b = a + d
    print((a, b))
    d -= 2
d = m - 1
for i in range(m):
    if d <= 0:
        break
    a = r + i + 1
    b = a + d
    print((a, b))
    d -= 2
