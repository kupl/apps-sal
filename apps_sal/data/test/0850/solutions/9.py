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
MAX = 100
k = RI()
d = RI()
cnt = [0] * 5
a = []
for i in d:
    if i == 0:
        cnt[0] = 1
    elif i == 100:
        cnt[1] = 1
    elif i < 10:
        cnt[2] = i
    elif i % 10 == 0:
        cnt[3] = i
    else:
        cnt[4] = i
if cnt[0]:
    a.append(0)
if cnt[1]:
    a.append(100)
if cnt[2]:
    a.append(cnt[2])
if cnt[3]:
    a.append(cnt[3])
elif not cnt[2] and not cnt[3] and cnt[4]:
    a.append(cnt[4])
print(len(a))
print(*a)
