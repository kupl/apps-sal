import getpass
import sys
import math
import itertools
import bisect


def lcm(a, b):
    return a * b // math.gcd(a, b)


def ria():
    return [int(i) for i in input().split()]


def dr(v):
    sm = sum([int(i) for i in str(v)])
    return sm if sm < 10 else dr(sm)


def range_sum(a, b):
    ass = (((b - a + 1) // 2) * (a + b))
    if (a - b) % 2 == 0:
        ass += (b - a + 2) // 2
    return ass


def comba(n, x):
    return (math.factorial(n) // math.factorial(n - x)) // math.factorial(x)


files = True
debug = False

if getpass.getuser() == 'frohenk' and files:
    debug = True
    sys.stdin = open("test.in")
    # sys.stdout = open('test.out', 'w')
    pass

g, d, f = ria()
gs = sorted(ria())
ds = sorted(ria())
fs = sorted(ria())

ar = []
for i in gs:
    ar.append((i, 0))
for i in ds:
    ar.append((i, 1))
for i in fs:
    ar.append((i, 2))
ar = sorted(ar)
suma = 0
for i, tp in ar:
    gl = bisect.bisect_right(gs, i * 2) - bisect.bisect_left(gs, i)
    dl = bisect.bisect_right(ds, i * 2) - bisect.bisect_left(ds, i)
    fl = bisect.bisect_right(fs, i * 2) - bisect.bisect_left(fs, i)
    if gl < 1 or dl < 2 or fl < 3:
        continue
    mp = 1
    if tp == 0:
        pass
    else:
        mp *= comba(gl, 1)

    if tp == 1:
        mp *= comba(dl - 1, 1)
    else:
        mp *= comba(dl, 2)

    if tp == 2:
        mp *= comba(fl - 1, 2)
    else:
        mp *= comba(fl, 3)
    suma += mp
print(suma)
