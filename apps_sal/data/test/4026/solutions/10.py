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


for _ in range(val()):
    n, m = li()
    l = []
    middle = 0
    for i in range(n):
        a, b = li()
        c, d = li()
        l.append([a, b, c, d])
        if b == c:
            middle = 1

    if m & 1 or not middle:
        print('NO')
        continue

    done = 0
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i][1] == l[j][2] and l[j][1] == l[i][2]:
                done = 1
    print('YES' if done else 'NO')
