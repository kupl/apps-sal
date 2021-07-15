# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 22:04:16 2020

@author: liang
"""

N = int(input())
A = [int(x) for x in input().split()]
d = [0]*N

for a in A:
    d[a-1] += 1
#print(d)
score = 0
for  a in d:
    score += a*(a-1)//2
#print(score)
for a in A:
    print(score - d[a-1] + 1)
