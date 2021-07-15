# -*- coding: utf-8 -*-
"""
Created on Tue May 17 15:26:55 2016

@author: Alex
"""
from sys import stdin

n,m = [int(i) for i in input().split()]
l = [int(i) for i in stdin.readline().split()]
prev = [-1 for i in range(n)]
re = []
for i in range(n-1):
    if l[i] != l[i+1]:
        prev[i+1] = i
    else:
        prev[i+1] = prev[i]
for _ in range(m):
    le,ri,xi = [int(i) for i in stdin.readline().split()]
    i = ri-1
    if l[i]!=xi:
        re.append(str(ri))
    else:
        if prev[i]<le-1:
            re.append('-1')
        else:
            re.append(str(prev[i]+1))
print('\n'.join(re))
        

