"""
Created on Tue Sep  8 20:45:37 2020

@author: liang
"""


def gcc(a, b):
    if b == 0:
        return a
    return gcc(b, a % b)


(A, B) = list(map(int, input().split()))
if A < B:
    (A, B) = (B, A)
print(A * B // gcc(A, B))
