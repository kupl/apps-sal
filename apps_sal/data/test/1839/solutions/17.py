3

import itertools as ittls
from collections import Counter

from pprint import pprint as pprint

import re
import math


def sqr(x):
    return x*x

def inputarray(func=int):
    return list(map(func, input().split()))

# --------------------------------------
# --------------------------------------

N = int(input())

maskrow = [0]*N
maskcol = [0]*N
res = []

for i in range(N*N):
    x, y = inputarray(lambda x: int(x) - 1)

    if maskrow[x] == 0 and maskcol[y] == 0:
        res.append(i)

        maskrow[x] = 1
        maskcol[y] = 1

print( ' '.join([str(x + 1) for x in res]) )

