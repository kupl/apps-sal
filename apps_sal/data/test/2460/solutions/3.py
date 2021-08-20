import sys
from math import *


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return map(int, minp().split())


(n, m) = mints()
a = list(mints())
b = list(mints())
l = [None] * (n + m)
r = [None] * (n + m)
c = [0] * (n + m)
x = None
for i in range(len(a)):
    l[i] = x
    if b[i] == 1:
        x = i
x = None
for i in range(len(a) - 1, -1, -1):
    r[i] = x
    if b[i] == 1:
        x = i
for i in range(len(a)):
    if b[i] == 0:
        aa = a[i]
        ll = l[i]
        rr = r[i]
        if ll == None:
            if rr != None:
                c[rr] += 1
        elif rr == None:
            c[ll] += 1
        elif aa - a[ll] <= a[rr] - aa:
            c[ll] += 1
        else:
            c[rr] += 1
for i in range(len(a)):
    if b[i] == 1:
        print(c[i], end=' ')
