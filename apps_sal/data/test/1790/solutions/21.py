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


n = int(input())
x = [0] * 1000
for _ in range(n):
    l = list(numIN())
    for i in l[1:]:
        x[i] += 1
z = []
for i in range(1000):
    if x[i] == n:
        z.append(str(i))
print(' '.join(z))
