#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time



(n, m) = (int(i) for i in input().split())
ans    = 0

for i in range(n):
    b = min([int(j) for j in input().split()])
    if b > ans:
        ans = b

start = time.time()

print(ans)
finish = time.time()
#print(finish - start)

