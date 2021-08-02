#!/usr/bin/env python

n = int(input())

seenx = set()
seeny = set()
xs = []
ys = []

for _ in range(4 * n + 1):
    x, y = list(map(int, input().strip().split()))
    seenx.add(x)
    seeny.add(y)
    xs.append(x)
    ys.append(y)

badx, bady = -1, -1

minx = min(xs)
maxx = max(xs)
if xs.count(minx) < n:
    badx = minx
    bady = ys[xs.index(minx)]
elif xs.count(maxx) < n:
    badx = maxx
    bady = ys[xs.index(maxx)]
miny = min(ys)
maxy = max(ys)
if bady == -1:
    if ys.count(miny) < n:
        bady = miny
        badx = xs[ys.index(miny)]
    elif ys.count(maxy) < n:
        bady = maxy
        badx = xs[ys.index(maxy)]

if badx == -1:  # the point is inside the square
    for i, x in enumerate(xs):
        if x not in (minx, maxx) and ys[i] not in (miny, maxy):
            badx = x
            bady = ys[i]
            break

print(badx, bady)
