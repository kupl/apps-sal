#!/usr/bin/env python 3

import sys

n = sys.stdin.read()
a = n.split()

n = int(a[0])
k = int(a[1])

if k <= (n + 1) // 2:
    print(2 * k - 1)
else:
    print((k - (n + 1) // 2) * 2)

