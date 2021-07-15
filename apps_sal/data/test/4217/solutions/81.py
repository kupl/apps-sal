import sys
import copy
import math
import itertools
import numpy as np
l = [int(c) for c in input().split()]
N = l[0]
M = l[1]
KA = [list(map(int,input().split())) for c in range(N)]

F = [0]*M

for i in range(N):
    for j in range(1,KA[i][0]+1):
        F[KA[i][j]-1]+=1
print(F.count(N))
