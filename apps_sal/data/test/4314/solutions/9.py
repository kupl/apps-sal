import sys
import copy
import math
import itertools
import numpy as np

H,W = [int(c) for c in input().split()]
a = np.array([list(input()) for c in range(H)])
b = copy.deepcopy(a)
Hc=[]
Wc=[]
for i in range(H):
    if np.count_nonzero(a[i,:] == ".") == W:
        Hc.append(i)

for i in range(W):
    if np.count_nonzero(a[:,i] == ".") == H:
        Wc.append(i)

a = np.delete(a,Hc,0)
a = np.delete(a,Wc,1)

for i in range(len(a)):
    s = ""
    for j in range(len(a[i])):
        s+=a[i][j]
    print(s)
