from bisect import bisect_left as bl
from bisect import bisect_right as br
from heapq import heappush,heappop,heapify
import math
from collections import *
from functools import reduce,cmp_to_key
import sys
input = sys.stdin.readline

from itertools import accumulate
from functools import lru_cache

M = mod = 998244353
def factors(n):return sorted(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
def inv_mod(n):return pow(n, mod - 2, mod)
 
def li():return [int(i) for i in input().rstrip('\n').split()]
def st():return input().rstrip('\n')
def val():return int(input().rstrip('\n'))
def li2():return [i for i in input().rstrip('\n')]
def li3():return [int(i) for i in input().rstrip('\n')]


def givesum(n):return sum([int(i) for i in str(n)])

for _ in range(val()):
    n, s = li()
    ans = 0
    curr = 10
    while givesum(n) > s:
        temp = n % curr
        n += curr - temp
        ans += curr - temp
        curr *= 10
    print(ans)

