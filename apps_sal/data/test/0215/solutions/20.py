#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
"""

# import {{{
from collections import ChainMap
from collections import Counter
from collections import defaultdict
from collections import deque
from collections import namedtuple
import bisect
import copy
import decimal
import fractions
import functools
import heapq
import itertools
import math
import operator
import pprint
import random
import re
import sys
import time

try:
    import numpy as np
    import scipy as sp
except:
    pass
# }}}

# util {{{
def is_odd(x):
    return x % 2 == 1

def is_even(x):
    return x % 2 == 0

def cmp(x, y):
    return (x > y) - (x < y)

def sgn(x):
    return cmp(x, 0)

def clamp(x, lo, hi):
    assert lo <= hi
    if x < lo:
        return lo
    elif x > hi:
        return hi
    else:
        return x

def chmax(xmax, x):
    if x > xmax:
        return x, True
    else:
        return xmax, False

def chmin(xmin, x):
    if x < xmin:
        return x, True
    else:
        return xmin, False

sys.setrecursionlimit(100000)
# }}}

# 適宜調整
PINF = float("inf")
NINF = float("-inf")
EPS  = 1e-9



def main():
    N = int(input())
    S = input()

    sets = []

    s = set()
    for c in S:
        if c.isupper():
            if s:
                sets.append(s)
            s = set()
        else:
            s.add(c)
    if s:
        sets.append(s)

    ans = len(max(sets, key=len)) if sets else 0
    print(ans)

def __starting_point(): main()

__starting_point()
