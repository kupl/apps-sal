"""input
8
fced
xyz
r
dabcef
az
aa
bad
babc
"""
import sys
from collections import defaultdict as dd
from itertools import permutations as pp
from itertools import combinations as cc
from collections import Counter as ccd
from random import randint as rd
from bisect import bisect_left as bl
import heapq
mod = 10 ** 9 + 7


def ri(flag=0):
    if flag == 0:
        return [int(i) for i in sys.stdin.readline().split()]
    else:
        return int(sys.stdin.readline())


def ff(a):
    return ord(a) - ord('a')


for _ in range(ri(1)):
    a = list(input())
    a.sort()
    f = 1
    b = list(set(a))
    b.sort()
    if len(a) != len(b):
        f = 0
    for i in range(1, len(b)):
        if ff(b[i]) - ff(b[i - 1]) != 1:
            f = 0
    if f:
        print('Yes')
    else:
        print('No')
