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



n = val()
l = sorted(li())
if n <= 36:
    ans = float('inf')
    for i in range(1, 10 ** 5):
        curr = 0
        for j in range(n):
            curr += abs(l[j] - i ** j)
            if i ** j > 10 ** 10:
                curr = float('inf')
                break
        ans = min(ans, curr)
else:
    ans = 0
    for j in l:
        ans += abs(j - 1)
print(ans)
