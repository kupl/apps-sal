# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 02:37:37 2020

@author: liang
"""
"""
key = lambda x:x[1]
"""
N = int(input())
A = [int(i) for i in input().split()]
B = [(i+1,A[i]) for i in range(N)]
B.sort(key=lambda x: x[1])
#print(B)
res = [str(b[0]) for b in B]
#print(res)
print(' '.join(res))
