#!/usr/bin/env python3

import sys
from collections import Counter

n = int(input())
a = [int(x) for x in input().split()]

s = sum(a)
c1 = Counter(a)
c2 = Counter()

cur = 0
for x in a:
    c1[x] -= 1
    c2[x] += 1
    cur += x

    s1 = cur
    s2 = s - s1
    if s1 == s2:
        print('YES')
        return
    if (s2 - s1) % 2 == 1:
        continue
    if s2 > s1:
        if c1[(s2 - s1) // 2] > 0:
            print('YES')
            return
    else:
        if c2[(s1 - s2) // 2] > 0:
            print('YES')
            return

print('NO')
