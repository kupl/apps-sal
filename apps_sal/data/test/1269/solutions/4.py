from bisect import bisect_left as bl
from bisect import bisect_right as br
import heapq
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


n, m = li()
l = li()

l = [i - 1 for i in l]
mintill = [[0] * m for i in range(m)]
for i in range(n):
    curr = l[i]
    an = i
    for j in range(i + 1, m):
        if l[j] < curr:
            curr = l[j]
            an = j
        mintill[i][j] = an

score = [[-1] * (m + 1) for i in range(m + 1)]


def recursive(i, j):
    if score[i][j] != -1: return score[i][j]
    if i == j or i + 1 == j: return 1
    mincurr = mintill[i][j - 1]
    left = right = 0

    for k in range(i, mincurr + 1):
        left = (left + recursive(i, k) * recursive(k, mincurr)) % mod
    for k in range(mincurr + 1, j + 1):
        right = (right + recursive(mincurr + 1, k) * recursive(k, j)) % mod
    score[i][j] = left * right % mod
    return score[i][j]


print(recursive(0, m))
