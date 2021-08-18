from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from bisect import bisect_left, bisect_right
import sys
import math
import itertools
import fractions
sys.setrecursionlimit(10**8)
mod = 10**9 + 7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))


def prime_factorize(n):
    if n == 1:
        return [1]
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


n = inp()
c = Counter(prime_factorize(n))
res = 0
for k, v in c.items():
    if k == 1:
        continue
    cnt = 0
    for now in range(1, 150000):
        cnt += now
        if cnt > v:
            res += now - 1
            break
print(res)
