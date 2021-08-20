import sys
from math import *


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return list(map(int, minp().split()))


(n, x) = mints()
e = [[] for i in range(n)]
for i in range(n - 1):
    (a, b) = mints()
    e[a - 1].append(b - 1)
    e[b - 1].append(a - 1)
x -= 1
q = [0] * n
d = [0] * n
p = [-1] * n
ql = 0
qr = 1
q[0] = x
d[x] = 1
while ql < qr:
    u = q[ql]
    ql += 1
    for v in e[u]:
        if d[v] == 0:
            d[v] = d[u] + 1
            p[v] = u
            q[qr] = v
            qr += 1
dd = [0] * n
ql = 0
qr = 1
q[0] = 0
dd[0] = 1
while ql < qr:
    u = q[ql]
    ql += 1
    for v in e[u]:
        if dd[v] == 0:
            dd[v] = dd[u] + 1
            q[qr] = v
            qr += 1
r = 0
for i in range(n):
    if d[i] < dd[i]:
        r = max(r, dd[i])
print((r - 1) * 2)
