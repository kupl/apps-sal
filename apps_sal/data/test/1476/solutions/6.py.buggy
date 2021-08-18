#!/usr/bin/env python

import sys

n = int(input())

if n == 4:
    print(4)
    print(3, 1, 4, 2)
    return

out = []

for i in range(0, n, 2):
    out.append(i + 1)
if not abs(out[-1] - 2) == 1:
    for i in range(1, n, 2):
        out.append(i + 1)

print(len(out))
print(' '.join(map(str, out)))
