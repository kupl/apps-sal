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

mx = -1
x = -1
for i in l:
    d[i] += 1
    if d[i] > mx:
        mx = d[i]
        x = i
i = l.index(x)
ans = []
for j in range(i, 0, -1):
    if l[j] > l[j - 1]:
        l[j - 1] += abs(l[j] - l[j - 1])
        ans.append([1, j, j + 1])
    elif l[j] < l[j - 1]:
        l[j - 1] -= abs(l[j] - l[j - 1])
        ans.append([2, j, j + 1])
    else:
        coninue
for j in range(i, n - 1):
    if l[j + 1] > l[j]:
        l[j + 1] -= abs(l[j] - l[j + 1])
        ans.append([2, j + 2, j + 1])
    elif l[j + 1] < l[j]:
        l[j + 1] += abs(l[j] - l[j + 1])
        ans.append([1, j + 2, j + 1])
    else:
        continue
print(len(ans))
for i in ans:
    print(*i)
