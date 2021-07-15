#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

#   = input()
n   = int(input())

#() = (i for i in input().split())
#   = [i for i in input().split()]

d1 = {}
d2 = {}

for i in range(n):
    (x, y) = (int(i) for i in input().split())
    t = x - y
    if t in list(d1.keys()):
        d1[t] +=1
    else:
        d1[t] = 1

    t = x+y
    if t in list(d2.keys()):
        d2[t] +=1
    else:
        d2[t] = 1

start = time.time()

ans = 0

for i in list(d1.keys()):
    ans += d1[i]*(d1[i]-1)//2

for i in list(d2.keys()):
    ans += d2[i]*(d2[i]-1)//2

print(ans)
finish = time.time()
#print(finish - start)

