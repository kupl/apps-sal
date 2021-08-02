from bisect import bisect_right as br
from bisect import bisect_left as bl
from collections import *
from itertools import *
import functools
import sys
import math
import random
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


def numIN(x=" "):
    return(map(int, sys.stdin.readline().strip().split(x)))


def charIN():
    return(sys.stdin.readline().strip().split())


def dis(x, y):
    a = y[0] - x[0]
    b = x[1] - y[1]
    return (a * a + b * b)**0.5


n = int(input())
l = list(numIN())
d = defaultdict(int)

for i in l:
    d[i] += 1
    if d[i] > 2:
        print('NO')
        return

l.sort()
ans1 = []
ans2 = []
for i in l:
    if d[i] == 2:
        ans1.append(i)
        ans2.append(i)
        d[i] = 0
    elif d[i] == 1:
        ans1.append(i)
        d[i] = 0
ans1.sort()
ans2.sort(reverse=True)

print('YES')
print(len(ans1))
print(*ans1)
print(len(ans2))
print(*ans2)
