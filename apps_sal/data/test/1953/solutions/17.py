#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input())
x = [ int(i) for i in input().split() ]

x = sorted(x)

m = 0
s = 0

for i in x:
    if s <= i:
        m += 1
        s += i

print(m)

