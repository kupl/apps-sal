"""
Created on Sun Sep 27 02:46:15 2020

@author: liang
"""

from collections import deque

n = int(input())
A = [int(x) for x in input().split()]

res = deque()

for i in range(n):
    if i % 2 == 0:
        res.append(A[i])
    else:
        res.appendleft(A[i])

if n % 2 == 1:
    print(" ".join(map(str, reversed(res))))
else:
    print(" ".join(map(str, res)))
