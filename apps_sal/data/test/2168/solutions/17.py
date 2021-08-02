#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 14:00:51 2018

@author: mach
"""

i = int(input())
l = []
for _ in range(i):
    k = list(map(int, input().strip().split()))
    l.append(k)

# //l = [[2,4,3],[2,2,1],[3,1,1,1]]
l.sort(key=lambda x: max(x[1:]), reverse=True)
k = max(l[0][1:])
sums = 0
for i in range(1, len(l)):
    j = (k - max(l[i][1:])) * (len(l[i]) - 1)
    sums += j

print(sums)
