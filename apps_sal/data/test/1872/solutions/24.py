import os
import sys
import pdb
import time
import calendar
import datetime
import math
import itertools
import operator as op
from functools import reduce


def ncr(n, r):
    r = min(r, n - r)
    numer = reduce(op.mul, list(range(n, n - r, -1)), 1)
    denom = reduce(op.mul, list(range(1, r + 1)), 1)
    return numer // denom


n, r = list(map(int, input().split()))
s = 2 * r * math.sin(math.pi / n)
Apoly = 1 / (4 * math.tan(math.pi / n))
Asub = math.tan(math.pi * (1 / 2 - 3 / (2 * n))) / 4

print(n * s**2 * (Apoly - Asub))
