

import array
from bisect import *
from collections import *
import fractions
import heapq
from itertools import *
import math
import random
import re
import string
import sys

L = int(input())

v = 1
edges = []

n = 2
cost = 1
while n <= L:
    edges.append((v, v + 1, 0))
    edges.append((v, v + 1, cost))
    cost *= 2
    v += 1
    n *= 2

v_sink = v

n //= 2
N = n
L -= N

while L > 0:
    if L >= n:
        edges.append((v, v_sink, N))
        L -= n
        N += n
    n //= 2
    v -= 1

print(v_sink, len(edges))
for e in edges:
    print(*e)
