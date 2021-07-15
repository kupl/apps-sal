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



def check(diff, x, y, n):
    s = set()
    i = y
    while n and i > 0:
        s.add(i)
        i -= diff
        n -= 1
    i = y + diff
    while n:
        n -= 1
        s.add(i)
        i += diff
    
    return -1 if x not in s else max(s)


for _ in range(val()):
    n, x, y = li()


    diff = factors(y - x)

    for i in range(1, y - x + 1):
        ans = check(i, x, y, n)
        if ans != -1:
            diff = i
            break
    

    l = []
    while n:
        l.append(ans)
        n -= 1
        ans -= diff
    print(*l)
