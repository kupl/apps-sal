# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 20:45:37 2020

@author: liang
"""
"""
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)
"""

from math import gcd
A, B = map(int, input().split())
if A < B:
    A, B = B, A
print(A * B // gcd(A, B))
