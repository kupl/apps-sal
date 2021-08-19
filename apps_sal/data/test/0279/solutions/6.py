#!/usr/bin/env python

v1, v2 = list(map(int, input().split(' ')))
t, d = list(map(int, input().split(' ')))
t -= 1

total = v1

while (v1 + d) - ((t - 1) * d) <= v2 and t:
    v1 += d
    total += v1
    t -= 1

diff = v2 + (t - 1) * d - v1
if t:
    v1 += diff
    t -= 1
    total += v1

while t:
    t -= 1
    v1 -= d
    total += v1

print(total)

assert(v1 == v2)
