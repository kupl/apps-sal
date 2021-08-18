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
n, m = RI()
x, y = 0, 0
print(min(n, m) + 1)
if n < m:
    for i in range(n + 1):
        print(i, n - i)
else:
    for i in range(m + 1):
        print(i, m - i)
