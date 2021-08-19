import math
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
#################################################
x = RI()[0]
x %= 360
if x > 180:
    x = x - 360
ans = 0
val = abs(x)
for i in range(1, 4):
    x -= 90
    if x < -180:
        x = 360 + x
    if abs(x) < val:
        val = abs(x)
        ans = i
print(ans)
