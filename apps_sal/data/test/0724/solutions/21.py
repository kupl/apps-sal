#!/usr/bin/env python3
from sys import stdin, stdout

def rint():
    return list(map(int, stdin.readline().split()))
#lines = stdin.readlines()


x = [0 for i in range(101)]

n, d = rint()

xin = list(rint())
xin.sort()
for xx in xin:
    x[xx] += 1
if xin[-1] <= d+1:
    print(0)
    return
maxn = 0
for i in range(1,d+2):
    maxn += x[i]

cur = maxn
for i in range(d+2, 101):
    cur = cur - x[i-d-1] + x[i]
    if cur > maxn:
        maxn = cur

print(n-maxn)

