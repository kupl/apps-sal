#!/usr/bin/env python3

from collections import Counter

n = int(input())
a = Counter([int(x) for x in input().split()])
r = 0
for k, v in a.items():
    u = (1 << (k - 1).bit_length()) - k
    if u:
        if u in a:
            r += v * a[u]
    else:
        r += v * (v - 1) // 2
print(r)
