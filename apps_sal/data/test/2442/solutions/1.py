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

for _ in range(val()):
    n = val()
    l = sorted(li())

    a1 = set()
    a2 = set()
    for i in l:
        if i in a1:
            a2.add(i)
        else:a1.add(i)
    ans = 0
    for i in range(200):
        if i not in a1:
            ans += i
            break
    for i in range(200):
        if i not in a2:
            ans += i
            break
    print(ans)
