#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#n = int(input())
from math import ceil

n, k = list(map(int, input().split()))
arr = list(map(int, list(input().split())))

d = {}
max_cnt = 0


for i in range(len(arr)):
    x = arr[i]
    if not x in d:
        d[x] = 0
    d[x] += 1
    max_cnt = max(max_cnt, d[x])

min_blud = ceil(max_cnt / k)
print(min_blud * len(d) * k - n)

