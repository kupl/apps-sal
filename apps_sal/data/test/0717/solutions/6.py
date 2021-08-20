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


def distance_sqr(p0, p1):
    return (p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2


n = ri()
curD = 1
for i in range(n):
    (s, d) = ria()
    while s > curD or (curD - s) % d != 0:
        curD += 1
    curD += 1
print(curD - 1)
