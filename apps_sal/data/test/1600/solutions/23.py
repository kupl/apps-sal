#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter

n = int(input())
H = list(map(int,input().split()))
_H = sorted(H)

diff = Counter()
count = 0

for i in range(n):
    diff[H[i]] += 1
    diff[_H[i]] -= 1

    if _H[i] in diff and diff[_H[i]] == 0:
        diff.pop(_H[i])
    if H[i] in diff and diff[H[i]] == 0:
        diff.pop(H[i])
    if diff == Counter():
        count += 1

print(count)

