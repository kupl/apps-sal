import numpy
import statistics
import bisect
from sys import stdin
import sys
import math
from functools import reduce
import functools
import itertools
from collections import deque, Counter, defaultdict
from operator import mul
import copy
import heapq
sys.setrecursionlimit(10 ** 6)
INF = 10 ** 18
mod = 10 ** 9 + 7
(A, B) = map(int, input().split())


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr


c = math.gcd(A, B)
d = factorization(c)
if c > 1:
    print(len(d) + 1)
else:
    print(1)
