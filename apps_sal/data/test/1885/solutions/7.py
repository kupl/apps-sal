import re
import sys
import string
import operator
import functools
import fractions
import collections
sys.setrecursionlimit(10 ** 7)
dX = [-1, 1, 0, 0, -1, 1, -1, 1]
dY = [0, 0, -1, 1, 1, -1, -1, 1]
RI = lambda x=' ': list(map(int, input().split(x)))
RS = lambda x=' ': input().rstrip().split(x)
mod = int(1000000000.0 + 7)
eps = 1e-06
n = RI()[0]
v = n * (n - 1) * (n - 2) * (n - 3) * (n - 4)
v1 = v // 120
v2 = v1 * (n - 5) // 6
v3 = v2 * (n - 6) // 7
print(v1 + v2 + v3)
