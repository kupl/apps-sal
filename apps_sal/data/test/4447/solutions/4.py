import os.path
import math
import sys
from queue import Queue
3


def log(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def ni():
    return list(map(int, input().split()))


def nio(offset):
    return [int(x) + offset for x in input().split()]


def nia():
    return list(map(int, input().split()))


def toString(aList, sep=' '):
    return sep.join((str(x) for x in aList))


def toMapInvertIndex(aList):
    return {k: v for (v, k) in enumerate(aList)}


(n, m) = ni()
a = nia()
nm = n // m
mmap = [[] for _ in range(m)]
for i in range(n):
    xx = a[i] % m
    mmap[xx].append(i)
move = []
destination = []
for i in range(m):
    ddu = mmap[i]
    x = len(ddu)
    destination.extend([i] * (nm - x))
    move.extend(ddu[nm:x])
ssum = 0
lenmove = len(move)
sMoveId = sorted(list(range(lenmove)), key=lambda k: a[move[k]] % m)
di = 0
for i in range(lenmove):
    moveId = sMoveId[i]
    s = a[move[moveId]] % m
    while destination[di] < s:
        destination.append(destination[di] + m)
        di += 1
    d = destination[di]
    di += 1
    ssum += d - s
    a[move[moveId]] += d - s
print(ssum)
print(toString(a))
