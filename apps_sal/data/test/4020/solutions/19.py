"""input
01:02
03:02
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


(h1, m1) = [int(i) for i in input().split(':')]
(h2, m2) = [int(i) for i in input().split(':')]
k1 = h1
k2 = m1
c = 0
while h1 != h2 or m1 != m2:
    m1 += 1
    if m1 == 60:
        h1 += 1
        m1 = 0
    c += 1
c = c // 2
while c:
    k2 += 1
    if k2 == 60:
        k1 += 1
        k2 = 0
    c -= 1
print('%02d:%02d' % (k1, k2))
