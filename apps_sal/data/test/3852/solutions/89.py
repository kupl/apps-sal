"""from collections import *
from itertools import *
from bisect import *
from heapq import *

import math
from fractions import gcd"""
import sys
#input = sys.stdin.readline

import copy

N = int(input())
Amoto = list(map(int, input().split()))
lst = []
A = copy.copy(Amoto)
_min = A[0]
minidx = 0
for i in range(1, N):
    if _min > A[i]:
        _min = A[i]
        minidx = i
if _min < 0:
    for i in range(N)[::-1]:
        while _min < A[i] and len(lst) <= 2 * N + 1:
            A[i] += _min
            lst.append([minidx + 1, i + 1])
        minidx = i
        _min = A[i]

    if len(lst) <= 2 * N:
        print((len(lst)))
        for i in lst:
            print((" ".join([str(x) for x in i])))
        return
A = copy.copy(Amoto)
_max = A[0]
maxidx = 0
lst = []
for i in range(1, N):
    if _max < A[i]:
        _max = A[i]
        maxidx = i
if _max > 0:
    for i in range(N):
        while _max > A[i] and len(lst) <= 2 * N + 1:
            A[i] += _max
            lst.append([maxidx + 1, i + 1])
        maxidx = i
        _max = A[i]
    if len(lst) <= 2 * N:
        print((len(lst)))
        for i in lst:
            print((" ".join([str(x) for x in i])))
        return
else:
    print((0))
