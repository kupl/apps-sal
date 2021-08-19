#!/usr/bin/env python
# coding=utf-8

n = int(input())
l = []
for i in range(n):
    x, y = list(map(int, input().split()))
    l += [(x + y, x - y)]
l.sort()
r = -2000000000
a = 0
for u in l:
    if u[1] >= r:
        a += 1
        r = u[0]
print(a)
