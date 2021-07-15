#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

n       = int(input())
table   = []

for i in range(n):
    table.append([int(i) for i in input().split()])

start = time.time()
ans   = 0

for i in range(n):
    buf = 0
    for j in range(n):
        if table[i] == table[j]:
            buf += 1
    if buf > ans:
        ans = buf

print(ans)
finish = time.time()
#print(finish - start)

