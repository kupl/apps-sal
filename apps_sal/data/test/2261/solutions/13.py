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


def inv(x):
    s = ""
    for i in x:
        s += "+*"[i == '+']
    return s


x = ['+']
n = RI()[0]
for i in range(n):
    t = []
    for j in range(len(x)):
        t.append(x[j] + x[j])
        t.append(x[j] + inv(x[j]))
    x = t
print(*x, sep='\n')
