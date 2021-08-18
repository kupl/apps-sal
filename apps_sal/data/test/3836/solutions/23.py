from sys import stdin, stdout
from math import sqrt
import math
import heapq
from itertools import accumulate

N = int(input())

f = {}
f['00'] = []
f['10'] = []
f['01'] = []
f['11'] = []

for i in range(N):
    s = [x for x in stdin.readline().split()]
    f[s[0]].append(int(s[1]))

for key in f:
    f[key].sort(reverse=True)


s_X = sum(f['11'])
X = len(f['11'])
Y = len(f['10'])
Z = len(f['01'])

m = min(Y, Z)

s_Y = [0] * len(f['10'])
s = 0
for i in range(len(f['10'])):
    s += f['10'][i]
    s_Y[i] = s
s_Z = [0] * len(f['01'])
s = 0
for i in range(len(f['01'])):
    s += f['01'][i]
    s_Z[i] = s

res = 0
s = 0
for W in range(X + 1):
    if W > len(f['00']):
        break
    if W >= 1:
        s += f['00'][W - 1]

    bound = X - W
    if Y > Z:
        tmp_Y = min(Y, Z + bound)
        tmp_Z = Z
    elif Y == Z:
        tmp_Y = Y
        tmp_Z = Z
    elif Y < Z:
        tmp_Y = Y
        tmp_Z = min(Z, Y + bound)

    calculate = s_X + s
    if tmp_Y > 0:
        calculate += s_Y[tmp_Y - 1]
    if tmp_Z > 0:
        calculate += s_Z[tmp_Z - 1]

    res = max(res, calculate)

print(res)
