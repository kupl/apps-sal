from bisect import *
from math import *
from heapq import *
from collections import *
import sys
sys.setrecursionlimit(100000000)


def input():
    return sys.stdin.readline()[:-1]


L = int(input())
n = int(log(L, 2))
es = []
m = min(n, 19)
for i in range(1, 20):
    es.append((i, i + 1, 0))
for i in range(m):
    es.append((i + 1, i + 2, 1 << i))
t = L - (1 << m)
for i in range(20):
    if t >> i & 1:
        L -= 1 << i
        es.append((i + 1, 20, L))
print((20, len(es)))
for (u, v, c) in es:
    print((u, v, c))
