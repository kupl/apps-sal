import os
import sys
import io
import functools
import copy
import math
GANS = []


def cmp(x, y):
    if x[1] == y[1]:
        return -(y[0] - x[0])
    return -(x[1] - y[1])


s = input()
ans = []
cur = []
ctr = []
pos = []
pv = [chr(0)]
pvc = chr(1)
for (p, i) in enumerate(s[::-1]):
    if cur and cur[-1] == i:
        f = True
        if len(cur) >= 2:
            if cur[-2] > i:
                f = False
            elif cur[-2] == i:
                if pos[-2] == p - 2:
                    f = False
                if pv[-1] >= i:
                    f = False
        if f and p == pos[-1] + 1:
            cur.pop()
            pos.pop()
            pv.pop()
            pvc = pv[-1]
        else:
            cur.append(i)
            pos.append(p)
            pv.append(pvc)
    else:
        if cur:
            pvc = cur[-1]
        cur.append(i)
        pos.append(p)
        pv.append(pvc)
    ctr.append(len(cur))
    if ctr[-1] > 10:
        ans.append(''.join(cur[-5:][::-1]) + '...' + ''.join(cur[:2][::-1]))
    else:
        ans.append(''.join(cur[::-1]))
for i in range(len(ans)):
    print(ctr[-i - 1], ans[-i - 1])
