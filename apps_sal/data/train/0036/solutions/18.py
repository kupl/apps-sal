import math
import random
import itertools
import collections
import sys
import time
import fractions
import os
import functools
import bisect


def timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print("Время выполнения функции: %f" % (time.time() - t))
        return res
    return tmp


def contains(l, elem):
    index = bisect.bisect_left(l, elem)
    if index < len(l):
        return l[index] == elem
    return False


n = int(input())

l = list(map(int, input().split(' ')))
q = int(input())
qs = list(map(int, input().split(' ')))

"""
n = 3
l = [5, 3, 4]
q = 12
qs = [i+1 for i in range(q)]
"""
"""
n = 5
l = [random.randint(0, 10) for i in range(n)]
q = random.randint(0, 15)
qs = [random.randint(0, 10) for i in range(q)]
l = sorted(l)
print(l)
print(qs)
"""


partials = list(itertools.accumulate(l))

for i in range(q):
    kuchka = bisect.bisect_left(partials, qs[i])
    print(kuchka + 1)
