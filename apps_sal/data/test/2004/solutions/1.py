import math
import re
import os
import string
import sys


def ria():
    return [int(i) for i in input().split()]


def ri():
    return int(input())


def rfa():
    return [float(i) for i in input().split()]


eps = 1e-09


def is_equal(a, b):
    return abs(a - b) <= eps


def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2)


n = ri()
ar = []
for i in range(1, n + 1):
    if i % 2 == 0:
        ar.append(i)
for i in range(1, n + 1):
    if i % 2 == 1:
        ar.append(i)
for i in range(1, n + 1):
    if i % 2 == 0:
        ar.append(i)
print(len(ar))
for i in ar:
    print(i, end=' ')
