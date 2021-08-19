"""
Created on Tue Sep  8 20:45:37 2020

@author: liang
"""
from math import gcd
'\ndef gcd(a,b):\n    if b == 0:\n        return a\n    return gcd(b, a%b)\n'
(A, B) = map(int, input().split())
if A < B:
    (A, B) = (B, A)
print(A * B // gcd(A, B))
