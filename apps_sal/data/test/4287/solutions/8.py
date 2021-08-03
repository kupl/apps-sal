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


sys.setrecursionlimit(10 ** 6)

a, n, m = li()
l = []
rain = defaultdict(int)
for i in range(n):
    c, b = li()
    for j in range(c, b):
        rain[(j, j + 1)] = 1


# print(rain)
umbrellas = [float('inf')] * (a + 5)
for i in range(m):
    c, b = li()
    umbrellas[c] = min(umbrellas[c], b)
# print(umbrellas[:a + 1])


@lru_cache(None)
def dp(i=0, umbon=0):
    # print(i, umbon)
    if i == a:
        if rain[(i - 1, i)]:
            if umbon:
                return umbon
            return float('inf')
        else:
            return umbon
    else:
        ans = float('inf')
        last = umbon
        if rain[(i - 1, i)]:
            umbon = min(umbon, umbrellas[i]) if umbon else umbrellas[i]
            if not last:
                last = float('inf')
            ans = min(ans, last + dp(i + 1, umbon))
            ans = min(ans, last + dp(i + 1, 0))
        else:
            ans = min(ans, dp(i + 1, 0) + last)
            umbon = min(umbon, umbrellas[i]) if umbon else umbrellas[i]
            ans = min(ans, dp(i + 1, umbon) + last)
    return ans


print(dp(0, 0) if dp(0, 0) != float('inf') else -1)
