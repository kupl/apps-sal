# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 16:50:38 2020

@author: liang
"""
N = int(input())
d = dict()
ans = 0 
A = [int(input()) for _ in range(N)]
for a in A:
    if a in d:
        d[a] += 1
    else:
        d[a] = 1
#print(d)
for key in d.keys():
    if d[key] %2 ==1:
        ans += 1
        d[key] = 0
#print(d)
print(ans)
