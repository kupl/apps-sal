#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

#   = input()
n   = int(input())
a   = [int(i) for i in input().split()]

start = time.time()

s = sum(a)
if s == 0:
    ans = 0
elif s == 1:
    ans = 1
else:
    ans = 1

    l = 0
    while( a[l] != 1):
        l += 1

    r = l

    while(r < n-1):
        r += 1
        if a[r] == 1:
            ans *= (r-l)
            l = r

print(ans)
finish = time.time()
#print(finish - start)

