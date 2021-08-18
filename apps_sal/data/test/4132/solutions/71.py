"""
Created on Mon Sep 14 17:37:26 2020

@author: liang
"""
from math import gcd
N = int(input())
A = [int(x) for x in input().split()]


A.sort()
g = A[0]
for i in range(1, N):
    g = gcd(g, A[i])
print(g)
