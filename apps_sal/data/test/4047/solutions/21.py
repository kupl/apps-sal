"""input
5
2 2 2 3 3

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
odd = sum([i % 2 for i in a])
even = n - odd
print(min(even, odd))
