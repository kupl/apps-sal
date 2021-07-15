#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input())

l = list(map(int, input().split()))
d = l[1] - l[0]
arth = True
for i in range(n - 1):
    if l[i + 1] - l[i] != d:
        arth = False

if arth == True:
    print(l[n - 1] + d)
else:
    print(l[n - 1])

