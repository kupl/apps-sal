#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

#   = input()
n   = int(input())
x   = []
y   = []

for i in range(n):
    (X, Y) = (int(i) for i in input().split())
    x.append(X)
    y.append(Y)

start = time.time()

x = list(set(x))
y = list(set(y))

if len(x) < 2 or len(y) <2:
    print(-1)
else:
    ans = (x[1] - x[0])*(y[1] - y[0])
    if ans < 0:
        ans = -ans
    print(ans)

finish = time.time()
#print(finish - start)

