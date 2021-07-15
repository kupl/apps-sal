#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time


n   = int(input())
x   = []
y   = []

(x0, y0) = (int(i) for i in input().split())

for i in range(n):
    (x1, y1) = (int(i) for i in input().split())
    x.append(x1-x0)
    y.append(y1-y0)
    x0 = x1
    y0 = y1

start = time.time()

ans = 0
for i in range(n-1):
    if x[i]*y[i+1]-x[i+1]*y[i] > 0:
        ans += 1

if x[n-1]*y[0]-x[0]*y[n-1] > 0:
    ans += 1

print(ans)
finish = time.time()
#print(finish - start)

