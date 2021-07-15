#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

n   = int(input())

N   = [i for i in input()]
x   = [int(i) for i in input().split()]

start = time.time()

flag = False
ans  = float('Inf')

for i in range(n):
    if N[i] == 'R':
        left = i
        flag = True
    elif flag == True:
         buf = x[i] - x[left]
         if buf < ans:
             ans = buf
         flag = False

if ans < float('Inf'):
    print(ans//2)
else:
    print(-1)

finish = time.time()
#print(finish - start)

