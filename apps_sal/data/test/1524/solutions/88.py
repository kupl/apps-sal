import bisect
import collections
import copy
import heapq
import itertools
import math
import string
from collections import defaultdict as D
from functools import reduce
import numpy as np
import sys
import os
from operator import mul

sys.setrecursionlimit(10**7)


def _S(): return sys.stdin.readline().rstrip()
def I(): return int(_S())
def LS(): return list(_S().split())
def LI(): return list(map(int, LS()))


if os.getenv("LOCAL"):
    inputFile = basename_without_ext = os.path.splitext(os.path.basename(__file__))[0] + '.txt'
    sys.stdin = open(inputFile, "r")
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7

S = _S()
S += 'E'

ans = np.zeros(len(S) + 1, dtype='int')
bc = S[0]
count = 1

for i in range(1, len(S)):
    cc = S[i]
    if cc == bc:
        count += 1
        continue
    else:
        if cc == 'L':
            ans[i - 1] += math.ceil(count / 2)
            ans[i] += math.floor(count / 2)
            count = 1
            bc = 'L'
        else:
            ans[i - count] += math.ceil(count / 2)
            ans[i - count - 1] += math.floor(count / 2)
            count = 1
            bc = 'R'

print((*ans[:-2]))
