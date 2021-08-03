from sys import setrecursionlimit, exit
from math import ceil, floor, acos, pi
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from functools import reduce
import itertools
setrecursionlimit(10**7)
RI = lambda x=' ': list(map(int, input().split(x)))
RS = lambda x=' ': input().rstrip().split(x)
dX = [-1, 1, 0, 0, -1, 1, -1, 1]
dY = [0, 0, -1, 1, 1, -1, -1, 1]
mod = int(1e9 + 7)
eps = 1e-6
MAX = 1e9
#################################################
n, m, i, j, a, b = RI()
min_val = MAX
if (i, j) == (1, 1) or (i, j) == (1, m) or (i, j) == (n, 1) or (i, j) == (n, m):
    print(0)
else:
    if (n - i) % a == 0 and (m - j) % b == 0 and ((n - i) // a - (m - j) // b) % 2 == 0 and a <= n - 1 and b <= m - 1:
        min_val = min(min_val, max((n - i) // a, (m - j) // b))
    if (i - 1) % a == 0 and (m - j) % b == 0 and ((i - 1) // a - (m - j) // b) % 2 == 0 and a <= n - 1 and b <= m - 1:
        min_val = min(min_val, max((i - 1) // a, (m - j) // b))
    if (n - i) % a == 0 and (j - 1) % b == 0 and ((n - i) // a - (j - 1) // b) % 2 == 0 and a <= n - 1 and b <= m - 1:
        min_val = min(min_val, max((n - i) // a, (j - 1) // b))
    if (i - 1) % a == 0 and (j - 1) % b == 0 and ((i - 1) // a - (j - 1) // b) % 2 == 0 and a <= n - 1 and b <= m - 1:
        min_val = min(min_val, max((i - 1) // a, (j - 1) // b))
    if min_val == MAX:
        print("Poor Inna and pony!")
    else:
        print(min_val)
