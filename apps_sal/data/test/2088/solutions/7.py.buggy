from bisect import bisect_right as br
from bisect import bisect_left as bl
from collections import defaultdict
from itertools import combinations
import sys
import math
MAX = sys.maxsize
MAXN = 10**5 + 10
MOD = 10**9 + 7


def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False
    return True


def mhd(a, b, x, y):
    return abs(a - x) + abs(b - y)


def numIN():
    return(map(int, sys.stdin.readline().strip().split()))


def charIN():
    return(sys.stdin.readline().strip().split())


def bfs(g, d):
    nonlocal n

    for i in range(n, 0, -1):
        while g[i]:
            x = g[i].pop()
            d[i] += d[x]
    return d


n = int(input())
l = list(numIN())
if n == 1:
    print(1)
    return
if n == 2:
    print(1, 1)
    return
d = [0] * (n + 1)
l = [0, 0] + l
g = defaultdict(list)
for i in range(2, n + 1):
    g[l[i]].append(i)
    d[i] += 1
    d[l[i]] += 1
for i in range(1, n + 1):
    if g[i]:
        d[i] = 0
x = bfs(g, d)
x.sort()
for i in range(1, n + 1):
    print(x[i], end=' ')
