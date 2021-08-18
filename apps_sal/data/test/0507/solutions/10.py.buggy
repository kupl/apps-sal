#!/usr/bin/env python3
from sys import stdin, stdout


def rint():
    return list(map(int, stdin.readline().split()))
#lines = stdin.readlines()


n = int(input())

a = list(rint())
b = list(rint())

ii = []
for i in range(n):
    if a[i] != b[i]:
        ii.append(i)

if len(ii) == 2:
    if a[ii[0]] != a[ii[1]]:
        c = a[:]
    else:
        c = b[:]
    if c.count(c[ii[0]]) == 2:
        iii = ii[0]
    else:
        iii = ii[1]
else:
    c = a[:]
    iii = ii[0]


for i in range(n):
    if not i + 1 in c:
        c[iii] = i + 1
        print(*c)
        return
