#!/usr/bin/env python3
x, y, m = list(map(int, input().split()))
if not (x < y):
    x, y = y, x
if m <= y:
    print(0)
elif y <= 0:
    print(-1)
else:
    i = 0
    if x < 0:
        j = - (x // y)
        x += j * y
        i += j
    while y < m:
        x, y = y, x + y
        i += 1
    print(i)
