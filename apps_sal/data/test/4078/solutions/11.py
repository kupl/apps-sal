import collections
import atexit
import math
import sys
import bisect
sys.setrecursionlimit(1000000)


def getIntList():
    return list(map(int, input().split()))


try:
    import numpy

    def dprint(*args, **kwargs):
        print(*args, file=sys.stderr)
    dprint('debug mode')
except Exception:

    def dprint(*args, **kwargs):
        pass
inId = 0
outId = 0
if inId > 0:
    dprint('use input', inId)
    try:
        f = open('input' + str(inId) + '.txt', 'r')
        sys.stdin = f
    except Exception:
        dprint('invalid input file')
if outId > 0:
    dprint('use output', outId)
    try:
        f = open('stdout' + str(outId) + '.txt', 'w')
        sys.stdout = f
    except Exception:
        dprint('invalid output file')
    atexit.register(lambda: sys.stdout.close())
(N, M) = getIntList()
za = getIntList()
omin = min(za)
sg = [0 for i in range(N * 4)]
de = sg.copy()


def built_sg(root, left, right):
    if left == right:
        sg[root] = za[left]
        return sg[root]
    mid = (left + right) // 2
    a = built_sg(root * 2 + 1, left, mid)
    b = built_sg(root * 2 + 2, mid + 1, right)
    sg[root] = min(a, b)
    return sg[root]


def update(root, left, right, qleft, qright, dif):
    if qright < left or right < qleft:
        return sg[root]
    if qleft <= left and right <= qright:
        de[root] += dif
        sg[root] += dif
        return sg[root]
    if de[root] != 0:
        t = de[root]
        sg[root * 2 + 1] += t
        sg[root * 2 + 2] += t
        de[root * 2 + 1] += t
        de[root * 2 + 2] += t
        de[root] = 0
    mid = (left + right) // 2
    a = update(root * 2 + 1, left, mid, qleft, qright, dif)
    b = update(root * 2 + 2, mid + 1, right, qleft, qright, dif)
    sg[root] = min(a, b)
    return sg[root]


built_sg(0, 0, N - 1)
zm = []
zz = [0, N]
for i in range(M):
    (l, r) = getIntList()
    l -= 1
    r -= 1
    zm.append((l, r))
    zz.append(l)
    zz.append(r + 1)
zz.sort()
r = max(za) - sg[0]
zr = []
for i in range(len(zz) - 1):
    a = zz[i]
    b = zz[i + 1]
    if a == b:
        continue
    t = max(za[a:b])
    tzr = []
    for j in range(M):
        x = zm[j]
        if x[0] <= a <= x[1]:
            continue
        tzr.append(j + 1)
        update(0, 0, N - 1, x[0], x[1], -1)
    t1 = sg[0]
    if r < t - t1:
        r = t - t1
        zr = tzr
    for x in zm:
        if x[0] <= a <= x[1]:
            continue
        update(0, 0, N - 1, x[0], x[1], 1)
    assert omin == sg[0]
print(r)
print(len(zr))
for x in zr:
    print(x, end=' ')
