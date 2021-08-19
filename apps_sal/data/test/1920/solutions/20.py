#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

n = int(input())

f = []
m = []

for i in range(n):
    g, a, b = input().split()

    if g == "F":
        f.append([int(a), int(b)])
    else:
        m.append([int(a), int(b)])

maxi = 0

for i in range(1, 367):
    mw = 0
    mm = 0

    for j in range(len(f)):
        if f[j][0] <= i <= f[j][1]:
            mw += 1
    for j in range(len(m)):
        if m[j][0] <= i <= m[j][1]:
            mm += 1

    maxi = max(maxi, min(mw, mm))

print(maxi * 2)
