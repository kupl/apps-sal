from functools import lru_cache
from itertools import accumulate
from bisect import bisect_left as bl
from bisect import bisect_right as br
from heapq import heappush, heappop, heapify
import math
from collections import *
from functools import reduce, cmp_to_key
import sys
input = sys.stdin.readline


M = mod = 998244353
def factors(n): return sorted(set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
def inv_mod(n): return pow(n, mod - 2, mod)


def li(): return [int(i) for i in input().rstrip('\n').split()]
def st(): return input().rstrip('\n')
def val(): return int(input().rstrip('\n'))
def li2(): return [i for i in input().rstrip('\n')]
def li3(): return [int(i) for i in input().rstrip('\n')]


n = val()
l = li()

# l = list(accumulate(l))
d = {0: 1}

currsum = ans = 0
for i in range(n):
    currsum += l[i]
    if currsum in d:
        d = {}
        d[0] = 1
        d[l[i]] = 1
        ans += 1
        currsum = l[i]
    else:
        d[currsum] = 1
    # print(currsum)
print(ans)
