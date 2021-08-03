import bisect
import heapq
import itertools
import math
import operator
import os
import re
import string
import sys
from collections import Counter, deque, defaultdict
from copy import deepcopy
from decimal import Decimal
from fractions import gcd
from functools import lru_cache, reduce
from operator import itemgetter, mul, add, xor

import numpy as np

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7
# MOD = 998244353


N, A, B = list(map(int, sys.stdin.buffer.readline().split()))
if A * B < N:
    print((-1))
    return
if N < A + B - 1:
    print((-1))
    return

groups = [[] for _ in range(A)]
nums = deque(list(range(1, N + 1)))
for i in reversed(list(range(len(groups)))):
    groups[i].append(nums.pop())
for i in range(len(groups)):
    nums.append(groups[i].pop())
    for _ in range(B):
        if not nums:
            break
        groups[i].append(nums.popleft())

ans = []
for g in groups:
    ans += g[::-1]
print((*ans))
