from bisect import bisect_left, bisect_right, insort_left
from collections import Counter, defaultdict, deque
from heapq import heapify, heappop, heappush, heappushpop
from itertools import combinations, permutations
from math import gcd, factorial, log2
from pprint import pprint
from sys import setrecursionlimit
from time import time

setrecursionlimit(10**9)
MOD = 10**9 + 7
INF = 10**18

n, k = list(map(int, input().split()))
s = input()

memo = [[None] * n for _ in range(k + 1)]


def win(a, b):
    _a = s[a % n]
    _b = s[b % n]
    win
    if _a == _b:
        return a
    if _a == 'R':
        return a if _b == 'S' else b
    if _a == 'P':
        return a if _b == 'R' else b
    if _a == 'S':
        return a if _b == 'P' else b


cnt = 0


def recur(a, b):
    nonlocal cnt
    cnt += 1
    if memo[int(log2(b - a))][a % n] is not None:
        return a + memo[int(log2(b - a))][a % n]
    else:
        if b - a <= 2:
            winner = win(a, b - 1)
        else:
            winner = win(recur(a, (a + b) // 2), recur((a + b) // 2, b))
        memo[int(log2(b - a))][a % n] = winner % (b - a)
        return winner


print((s[recur(0, 2**k) % n]))
