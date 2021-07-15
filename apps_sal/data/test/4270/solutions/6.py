# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 21:55:15 2020

@author: liang
"""

N = int(input())
V = list(map(int,input().split()))
V.sort(reverse=True)
#print(V)
for i in range(N-1):
    tmp = 0
    tmp += (V.pop() + V.pop())/2
    V.append(tmp)

print(V[0])
