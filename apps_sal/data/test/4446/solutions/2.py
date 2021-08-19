#!/usr/bin/env python3
import math
import os
import sys
from atexit import register
from io import StringIO

# Buffered output, at least 2x faster.
sys.stdout = StringIO()
register(lambda: os.write(1, sys.stdout.getvalue().encode()))

###############################################################################
###############################################################################
n, a, b, k = [int(k) for k in sys.stdin.readline().split()]
hs = [int(k) for k in sys.stdin.readline().split()]


def uses(h):
    r = h % (a + b)
    if r == 0:
        r = a + b
    return int(math.ceil(r / a) - 1)


us = [uses(h) for h in hs]
us.sort()
ret = 0
for u in us:
    if u > k:
        break
    k -= u
    ret += 1
print(ret)
