from functools import reduce
from operator import *
from math import *
from sys import *
from string import *
from collections import *
setrecursionlimit(10**7)
dX = [-1, 1, 0, 0, -1, 1, -1, 1]
dY = [0, 0, -1, 1, 1, -1, -1, 1]
def RI(): return list(map(int, input().split()))
def RS(): return input().rstrip().split()


#################################################
n, k = RI()
v = [0] * k
a = RI()
for i in range(n):
    v[i % k] += a[i]
minInd = 0
for i in range(k):
    if v[i] < v[minInd]:
        minInd = i
print(minInd + 1)
