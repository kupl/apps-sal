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

n, m = list(map(int, input().split(" ")))

s = 0
for i in range(5):
    t1 = n//5
    t2 = m//5
    if i != 0:
        t1 += 1 if n % 5 >= i else 0
        t2 += 1 if m % 5 >= (5-i) else 0
    s += t1 * t2
print(s)

