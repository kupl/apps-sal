from collections import Counter, defaultdict, deque
from heapq import heappop, heappush, heapify
import sys
import bisect
import math
import itertools
import fractions
sys.setrecursionlimit(10**8)
mod = 10**9 + 7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))


def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


a = [0] * 100100
for i in range(1, 100010):
    tmp = 0
    if is_prime(i) and is_prime((i + 1) // 2):
        tmp = 1
    a[i] = a[i - 1] + tmp
q = inp()
for _ in range(q):
    l, r = inpl()
    print(a[r] - a[l - 1])
