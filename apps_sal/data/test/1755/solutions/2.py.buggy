from bisect import bisect_left as bl
from bisect import bisect_right as br
from heapq import heappush, heappop
import math
from collections import *
from functools import reduce, cmp_to_key, lru_cache


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


def give(i, j, mi, ma):
    # print(i, j, mi, ma)
    l1 = []
    for k in range(i, j + 1):
        if mi <= l[k] <= ma:
            ind = br(l1, l[k])
            if ind == len(l1):
                l1.append(l[k])
            else:
                l1[ind] = l[k]
    # print(j - i + 1, len(l1))
    return j - i - len(l1) + 1


n, k = li()
l = [0] + li()


if k:
    b = li()
else:
    b = []

for i in range(1, k):
    if l[b[i]] - l[b[i - 1]] < b[i] - b[i - 1] or l[b[i]] < l[b[i - 1]]:
        print(-1)
        return

for i in range(n + 1):
    l[i] -= i

if k:
    ans = give(1, b[0] - 1, -float('inf'), l[b[0]])
    ans += give(b[-1] + 1, n, l[b[-1]], float('inf'))

    for i in range(1, k):
        ans += give(b[i - 1], b[i], l[b[i - 1]], l[b[i]])


else:
    ans = give(1, n, -float('inf'), float('inf'))


print(ans)
