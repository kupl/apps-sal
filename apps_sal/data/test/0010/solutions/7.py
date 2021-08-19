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

n = int(input())

w = n // 7
d = n % 7
min_off = w * 2
max_off = w * 2
if d <= 2:
    max_off += d
elif 2 < d and d <= 5:
    max_off += 2
else:                           # d==6
    max_off += 2
    min_off += 1
print("{} {}".format(min_off, max_off))
