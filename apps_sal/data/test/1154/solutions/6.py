# coding: utf-8





import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect

def array2d(d1, d2, init = None):
    return [[init for _ in range(d1)] for _ in range(d2)]


n, h, k = list(map(int, input().split(" ")))
al = list(map(int, input().split(" ")))
in_proc = 0
pointer = 0
time = 0

for a in al:
    if a > h - in_proc:
        time += in_proc // k
        in_proc %= k
        if a > h - in_proc:
            time += 1
            in_proc = 0
    in_proc += a

time += in_proc // k
in_proc %= k
time += (in_proc > 0)
print(time)

