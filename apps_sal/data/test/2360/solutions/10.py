#!/usr/bin/env python3
from sys import stdin, stdout


def rint():
    return list(map(int, stdin.readline().split()))
#lines = stdin.readlines()


t = int(input())

for _ in range(t):
    n = int(input())
    lb, rb = 0, 0
    ct = 0
    ans = []
    for __ in range(n):
        lc, rc = rint()
        if lc >= ct:
            ans.append(lc)
            ct = lc + 1
        elif ct <= rc:
            ans.append(ct)
            ct += 1
        else:
            ans.append(0)

    print(*ans)
