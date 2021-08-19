from sys import stdin
import sys
from functools import lru_cache, cmp_to_key
from heapq import merge, heapify, heappop, heappush
# from math import *
from collections import defaultdict as dd, deque, Counter as C
from itertools import combinations as comb, permutations as perm
from bisect import bisect_left as bl, bisect_right as br, bisect
from time import perf_counter
from fractions import Fraction
import copy
import time
# import numpy as np
starttime = time.time()
# import numpy as np
mod = int(pow(10, 9) + 7)
mod2 = 998244353
def data(): return sys.stdin.readline().strip()
def out(*var, end="\n"): sys.stdout.write(' '.join(map(str, var)) + end)
def L(): return list(sp())
def sl(): return list(ssp())
def sp(): return list(map(int, data().split()))
def ssp(): return list(map(str, data().split()))
def l1d(n, val=0): return [val for i in range(n)]
def l2d(n, m, val=0): return [l1d(n, val) for j in range(m)]


try:
    # sys.setrecursionlimit(int(pow(10,6)))
    sys.stdin = open("input.txt", "r")
    # sys.stdout = open("../output.txt", "w")
except:
    pass

input = stdin.buffer.readline
def I(): return list(map(int, input().split()))


n, = I()
l = []
for i in range(n):
    l.append(I())
d = {}
su = {}
s = 0
an = [1, 1, 2, 1]
for i in range(n):
    for j in range(n):
        d[i - j] = d.get(i - j, 0) + l[i][j]
        su[i + j] = su.get(i + j, 0) + l[i][j]
x = 0
y = 0
for i in range(n):
    for j in range(n):
        p = d[i - j] + su[i + j] - l[i][j]
        if (i + j) % 2:
            if p > x:
                an[0], an[1] = i + 1, j + 1
                x = p
        else:
            if p > y:
                an[2], an[3] = i + 1, j + 1
                y = p
s = x + y
print(s)
print(*an)


endtime = time.time()
# print(f"Runtime of the program is {endtime - starttime}")
