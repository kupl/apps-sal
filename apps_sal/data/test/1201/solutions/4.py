import os
import sys
import re
from collections import OrderedDict

if 'PYCHARM' in os.environ:
    sys.stdin = open('in', 'r')

n = int(input())
things = []
for i in range(n):
    t, d, p = list(map(int, input().split()))
    things.append((d, t, p, i + 1))

things.sort()
D = 2001
f = [[0] * D]
w = [[False] * D]

for i in range(n):
    thing = things[i]
    w.append([False] * D)
    f.append(list(f[i]))
    for j in range(D):
        ni = j + thing[1]
        nv = f[i][j] + thing[2]
        if ni < thing[0]:
            if f[i + 1][ni] < nv:
                f[i + 1][ni] = nv
                w[i + 1][ni] = True

ind = 0
for i in range(D):
    if f[n][i] > f[n][ind]:
        ind = i

print(f[n][ind])
ans = []
for i in range(n, 0, -1):
    if w[i][ind]:
        ind -= things[i - 1][1]
        ans.append(things[i - 1][3])

print(len(ans))
print(*reversed(ans))




