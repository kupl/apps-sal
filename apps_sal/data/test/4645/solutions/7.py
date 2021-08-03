#!/usr/bin/env python3
from sys import stdin
import collections


def solve(tc):
    n = int(stdin.readline().strip())
    if n < 4:
        print(-1)
        return
    base = collections.deque()
    base.extend([2, 4, 1, 3])
    p = 5
    while p + 1 <= n:
        base.append(p)
        base.appendleft(p + 1)
        p += 2

    if p == n:
        base.append(p)

    for x in base:
        print(x, end=' ')
    print()


LOCAL_TEST = not __debug__
if LOCAL_TEST:
    infile = __file__.split('.')[0] + "-test.in"
    stdin = open(infile, 'r')

tcs = int(stdin.readline().strip())
tc = 1
while tc <= tcs:
    solve(tc)
    tc += 1
