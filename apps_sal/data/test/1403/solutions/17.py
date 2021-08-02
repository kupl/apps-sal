#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

(n, K) = (int(i) for i in input().split())
a = [int(i) for i in input().split()]

start = time.time()

a.sort()
ans = n

flag = 1
for i in range(1, n):
    if a[i - 1] == a[i]:
        flag += 1
    elif a[i] <= a[i - 1] + K:
        ans -= flag;
        flag = 1
    else:
        flag = 1

print(ans)
finish = time.time()
#print(finish - start)
