#!/bin/env python3

from sys import stdin
from collections import namedtuple

Guy = namedtuple('Guy', ['w', 'h'])

maxh1 = 0
maxh2 = 0

guys = []

sumw = 0
stdin.readline()
for line in stdin:
    try:
        w, h = map(lambda s: int(s.strip()), line.lstrip().split(' ', 1))
    except:
        continue
    guys.append(Guy(w, h))
    sumw += w
    if h >= maxh1:
        maxh2 = maxh1
        maxh1 = h
    elif h > maxh2:
        maxh2 = h

for g in guys:
    sq = (sumw - g.w)*(maxh1 if g.h != maxh1 else maxh2)
    print (sq, end=' ')

print()

