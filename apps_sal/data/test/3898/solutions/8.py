import math
import re
import sys
import string
import operator
import functools
import fractions
import collections
sys.setrecursionlimit(10**7)
RI = lambda x=' ': list(map(int, input().split(x)))
RS = lambda x=' ': input().rstrip().split(x)
dX = [-1, 1, 0, 0, -1, 1, -1, 1]
dY = [0, 0, -1, 1, 1, -1, -1, 1]
mod = int(1e9 + 7)
eps = 1e-6
pi = math.acos(-1.0)
MAX = 200010
#################################################
n = RI()[0]
a = RI()
b = RI()
a = [i for i in a if i]
b = [i for i in b if i]
if len(a) != len(b) or (len(a) == n and a != b):
    print("NO")
    return
ID = [0] * MAX
for i in range(len(a)):
    ID[a[i]] = (a[i - 1], a[(i + 1) % len(a)])
for i in range(len(b)):
    if ID[b[i]] != (b[i - 1], b[(i + 1) % len(b)]):
        print("NO")
        return
print("YES")
