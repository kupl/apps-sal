import re
import sys
import string
import operator
import functools
import fractions
import collections
from random import *
sys.setrecursionlimit(10**7)
dX = [-1, 1, 0, 0, -1, 1, -1, 1]
dY = [0, 0, -1, 1, 1, -1, -1, 1]
def RI(): return list(map(int, input().split()))
def RS(): return input().rstrip().split()


mod = 1e9 + 7
eps = 1e-6
#################################################
n = RI()[0]
a = RI()
ans = 1
for i in range(n - 1, 0, -1):
    if a[i - 1] > a[i]:
        break
    ans += 1
print(n - ans)
