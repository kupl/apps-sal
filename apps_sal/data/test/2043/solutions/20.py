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


def findMatch(a, b):
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            j += 1
        i += 1
    return i


s = RS()[0]
t = RS()[0]
x = findMatch(t, s)
y = len(t) - findMatch(t[::-1], s[::-1])
print(max(y - x + 1, 0))
