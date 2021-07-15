#!/usr/bin/env python3
from sys import stdin, stdout
from bisect import bisect, bisect_left

def rint():
    return list(map(int, stdin.readline().split()))
#lines = stdin.readlines()


n, m = rint()
a = list(rint())
b = list(rint())

c =[]
c.append(a[0])
for i in range(1,n):
    c.append(c[i-1]+a[i])

for i in range(m):
    ii = bisect_left(c, b[i])
    if ii == 0:
        print(1, b[i])
    else:
        print(ii+1,b[i] - c[ii-1])

