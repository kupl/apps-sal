from functools import reduce
from operator import *
from math import *
from sys import *
from string import *
from collections import *
setrecursionlimit(10**7)
dX = [-1, 1, 0, 0, -1, 1, -1, 1]
dY = [0, 0, -1, 1, 1, -1, -1, 1]
RI = lambda: list(map(int, input().split()))
RS = lambda: input().rstrip().split()
#################################################
t, sx, sy, ex, ey = RI()
needed = {c: 0 for c in 'NSEW'}
if sx < ex:
    needed['E'] = ex - sx
else:
    needed['W'] = sx - ex
if sy < ey:
    needed['N'] = ey - sy
else:
    needed['S'] = sy - ey
cnt = {c: 0 for c in 'NSEW'}
s = RS()[0]
for i in range(t):
    flag = 1
    if needed[s[i]]:
        cnt[s[i]] += 1
    for c in cnt:
        if cnt[c] < needed[c]:
            flag = 0
    if flag:
        print(i + 1)
        return
print(-1)
