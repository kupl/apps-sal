#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

(n, m) = (int(i) for i in input().split())

ans = 0


start = time.time()

for i in range(m):
    (x, d)  = (int(i) for i in input().split())
    ans += n*x
    if d > 0:
        ans +=d*((n-1)*n//2)
    else:
        if n%2 == 0:
            ans += d*n*n//4
        else:
            ans += d*(n+1)*(n-1)//4
print(ans/n)
finish = time.time()
#print(finish - start)

