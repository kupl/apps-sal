#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

a   = []

(r, c, n, k) = (int(i) for i in input().split())

for i in range(n):
    a.append([int(i)-1 for i in input().split()])

start   = time.time()
ans     = 0

for x1 in range(r):
    for y1 in range(c):
        for x0 in range(x1+1):
            for y0 in range(y1+1):
                now = 0
                for i in range(n):
                    if (a[i][0] >= x0) and  (a[i][0] <= x1) and (a[i][1] >= y0) and  (a[i][1] <= y1):
                        now +=1

                if now >= k:
                    ans += 1


print(ans)
finish = time.time()
#print(finish - start)

