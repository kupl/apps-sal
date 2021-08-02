# -*- coding: utf-8 -*-
n, x, t = map(int, input().split())
k = n // x
if n % x == 0:
    time = k * t
else:
    time = t * (k + 1)
print(time)
