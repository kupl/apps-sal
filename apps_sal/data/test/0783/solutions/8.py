#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

n   = int(input())
A   = [int(i) for i in input().split()]

start = time.time()

A   = [ A[n-i-1] for i in range(n)]
ans = [ 0 for i in range(n) ]

m   = 0
for i in range(n):
    if A[i] > m:
        m = A[i]
    else:
        ans[i] = 1+m-A[i]

for i in range(n):
    print(ans[n-1-i], end=' ')
print()
finish = time.time()
#print(finish - start)

