import numpy as np
from itertools import product

N = int(input())
info = []
for i in range(N):
    a = int(input())
    for __ in range(a):
        x,y = list(map(int,input().split()))
        info.append((i,x-1,y))

A = np.array(list(product([0,1], repeat=N)),np.bool)
for i, x, y in info:
    bl = (~A[:,i]) | (A[:,x] == bool(y))
    A = A[bl]
print((A.sum(axis=1).max()))

