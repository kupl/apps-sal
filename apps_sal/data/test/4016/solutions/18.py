from collections import defaultdict, deque
import sys
import heapq
import bisect
import math
import itertools
import string
import queue
import datetime
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
mod = 10 ** 9 + 7
eps = 10 ** (-7)


def inpl():
    return list(map(int, input().split()))


def inpl_s():
    return list(input().split())


(n, k) = inpl()
S = input()
for i in reversed(list(range(n))):
    if S[:i] == S[n - i:]:
        break
ans = S
for _ in range(k - 1):
    ans += S[i:]
print(ans)
