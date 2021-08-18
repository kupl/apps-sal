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


n = RI()[0]
ind = 0
ans1, ans2 = 10**6, 10**6
for i in range(4):
    a, b, c, d = RI()
    a = min(a, b)
    c = min(c, d)
    if a + c < ans1 + ans2:
        ind = i + 1
        ans1 = a
        ans2 = c
if n - ans1 < ans2:
    print(-1)
else:
    print(ind, ans1, n - ans1)
