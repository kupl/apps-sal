import re
import sys
import string
import operator
import functools
import fractions
import collections
sys.setrecursionlimit(10**7)
dX = [-1, 1, 0, 0, -1, 1, -1, 1]
dY = [0, 0, -1, 1, 1, -1, -1, 1]
RI = lambda x=' ': list(map(int, input().split(x)))
RS = lambda x=' ': input().rstrip().split(x)
mod = int(1e9 + 7)
eps = 1e-6
n = RI()[0]
v1 = 1
v2 = 1
for i in range(n - 1):
    v1 *= (6 + i)
    v2 *= (4 + i)
for i in range(1, n):
    v1 //= i
    v2 //= i
print(v1 * v2)
