#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

n   = int(input())
x   = [int(i) for i in input().split()]

start = time.time()

print(x[1]-x[0], x[n-1]-x[0])

for i in range(1, n-1):
    min_i = min(x[i] - x[i-1], x[i+1] - x[i])
    max_i = max(x[i] - x[0], x[n-1] - x[i])
    print(min_i, max_i)

print(x[n-1]-x[n-2], x[n-1]-x[0])

finish = time.time()
#print(finish - start)

