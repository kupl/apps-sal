#!/usr/bin/env python3

from collections import defaultdict


def hd(s):
    d, h = 0, 0
    dmax = 0
    for c in s:
        if c == '(':
            h += 1
            d -= 1
        else:
            h -= 1
            d += 1
            dmax = max(d, dmax)
    return h, dmax


n = int(input().strip())
h0 = 0
hp = defaultdict(int)
hm = defaultdict(int)
for _ in range(n):
    s = input().strip()
    h, d = hd(s)
    if h == d == 0:
        h0 += 1
    elif h > 0 and d == 0:
        hp[h] += 1
    elif h < 0 and h + d <= 0:
        hm[-h] += 1

res = h0 ** 2
for k, v in list(hp.items()):
    if k in hm:
        res += v * hm[k]


print(res)
