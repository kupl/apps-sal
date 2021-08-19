"""input
4
1 1 2 2
"""
import sys
from collections import defaultdict as dd
from itertools import permutations as pp
from itertools import combinations as cc
from collections import Counter as ccd
from random import randint as rd
from bisect import bisect_left as bl
from heapq import heappush as hpush
from heapq import heappop as hpop
mod = 10 ** 9 + 7


def ri(flag=0):
    if flag == 0:
        return [int(i) for i in sys.stdin.readline().split()]
    else:
        return int(sys.stdin.readline())


n = ri(1)
a = ri()
a.sort(reverse=True)
ans = 0
first = 0
if n % 2 == 1:
    for i in range(n // 2 + 1):
        first += a[i]
else:
    for i in range(n // 2):
        first += a[i]
second = sum(a) - first
print(first ** 2 + second ** 2)
