# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List

"""
created by shhuan at 2020/1/14 22:42

"""



def solve(A, B):

    b = B
    blen = 0
    while b > 0:
        blen += 1
        b //= 10
    if B != 10**blen-1:
        blen -= 1
    return A * blen


T = int(input())
for ti in range(T):
    a, b = map(int, input().split())
    print(solve(a, b))
