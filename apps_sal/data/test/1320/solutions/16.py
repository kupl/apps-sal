#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time


n   = int(input())
a   = [ 0 for i in range(n) ]
ans = 0

for i in range(n):
    str = input()
    m   = 0

    for j in range(n):
        if str[j] == 'C':
            m += 1
            a[j] += 1
    ans += m*(m-1)

start = time.time()

for i in range(n):
    ans += a[i]*(a[i]-1)

print(ans//2)
finish = time.time()
#print(finish - start)

