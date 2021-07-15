#!/usr/bin/env python

from sys import stdin

n = int(stdin.readline())
a1 = [int(x) for x in stdin.readline().split()]
a2 = [int(x) for x in stdin.readline().split()]
b = [int(x) for x in stdin.readline().split()]

cum1 = a1[:]
cum2 = a2[:]
for i in range(1, n - 1):
    cum1[i] += cum1[i-1]
for i in range(n - 3, -1, -1):
    cum2[i] += cum2[i+1]

min1, min2 = 1000000, 1000000
for i in range(n):
    c = b[i]
    if i:
        c += cum1[i-1]
    if i < n-1:
        c += cum2[i]

    if c <= min1:
        min2 = min1
        min1 = c
    elif c < min2:
        min2 = c

print(min1 + min2)
