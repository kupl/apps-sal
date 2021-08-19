import sys
import math
import string
import fractions
import functools
import collections
sys.setrecursionlimit(10**7)
RI = lambda x=' ': list(map(int, input().rstrip().split(x)))
RS = lambda x=' ': input().rstrip().split(x)
dX = [-1, 1, 0, 0, -1, 1, -1, 1]
dY = [0, 0, -1, 1, 1, -1, -1, 1]
mod = int(1e9 + 7)
eps = 1e-6
MAX = 1010
#################################################
ans = 0
m, n = RI()
for i in range(1, m + 1):
    ans += i * (pow(i / m, n) - pow((i - 1) / m, n))
print("%.12f" % ans)
