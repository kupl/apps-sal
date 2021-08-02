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


def array2d(d1, d2, init=None):
    return [[init for _ in range(d2)] for _ in range(d1)]


n = int(input())

cnt_m = 0
cnt_c = 0

for i in range(n):
    m, c = list(map(int, input().split(" ")))
    if m > c:
        cnt_m += 1
    elif m < c:
        cnt_c += 1

if cnt_m > cnt_c:
    print("Mishka")
elif cnt_m == cnt_c:
    print("Friendship is magic!^^")
else:
    print("Chris")
