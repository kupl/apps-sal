#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

"""
549 C
"""

n = int(input())
d = [1 for i in range(n+1)]

for i in range(1, n+1):
    pi, ci = list(map(int, input().split()))
    if ci == 0:
        d[i] = 0
        if pi != -1:
            d[pi] = 0

e = []
for i in range(1, n+1):
    if d[i] == 1:
        e.append(i)

if len(e) == 0:
    print(-1)
    quit()
else:
    print(" ".join(map(str, e)))

