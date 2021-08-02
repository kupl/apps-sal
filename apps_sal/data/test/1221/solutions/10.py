#!/usr/bin/env python3
from sys import stdin, stdout


def rint():
    return list(map(int, stdin.readline().split()))
#lines = stdin.readlines()


n, m = rint()

a = []
b = []
a = list(rint())
b = list(rint())

Max = -10**1000
maxi = -1
for i in range(n):
    for j in range(m):
        if Max < a[i] * b[j]:
            Max = a[i] * b[j]
            maxi = i
Max = -10**1000
for i in range(n):
    if i == maxi:
        continue
    for j in range(m):
        if Max < a[i] * b[j]:
            Max = a[i] * b[j]

print(Max)
