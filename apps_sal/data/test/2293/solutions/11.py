import math
import re
import sys
from collections import defaultdict
from heapq import heappush, heappop
from fractions import gcd


def read(type=int):
    return type(input())


def read_list(type=int, split=' ', F=None):
    if F:
        return map(lambda x: F(type(x)), raw_input().split(split))
    return list(map(type, input().split(split)))


def read_list_of_list(N, type=int, split=' ', F=None):
    return [read_list(type, F=F) for _ in range(N)]


m, n = read_list()
B = read_list_of_list(m)
L = []
for b in B:
    b = set(b[1:])
    for l in L:
        if l.isdisjoint(b):
            print('impossible')
            return
    L += [b]

print('possible')
