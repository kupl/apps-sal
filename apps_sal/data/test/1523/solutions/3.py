from bisect import bisect_right as br
from bisect import bisect_left as bl
from collections import defaultdict
from itertools import combinations
import sys
import math
MAX = sys.maxsize
MAXN = 10 ** 5 + 10
MOD = 10 ** 9 + 7


def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False
    return True


def mhd(a, b, x, y):
    return abs(a - x) + abs(b - y)


def numIN():
    return list(map(int, sys.stdin.readline().strip().split()))


def charIN():
    return sys.stdin.readline().strip().split()


(n, k) = numIN()
a = list(numIN())
b = list(numIN())
x = [0] * MAXN
d = {}
for i in range(n):
    if not x[a[i]]:
        x[a[i]] = 1
        d[a[i]] = [b[i]]
    else:
        d[a[i]].append(b[i])
rem = x[1:k + 1].count(0)
l = []
for i in list(d.keys()):
    z = len(d[i])
    if z > 1:
        d[i].sort()
        l += d[i][:z - 1]
l.sort()
print(sum(l[:rem]))
