from bisect import bisect_right as br
from bisect import bisect_left as bl
from collections import defaultdict
from itertools import combinations
import sys
import math
MAX = sys.maxsize
MAXN = 10**6 + 10
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
    return(list(map(int, sys.stdin.readline().strip().split())))


def charIN():
    return(sys.stdin.readline().strip().split())


t = [(-1, -1)] * 1000010


def create(a):
    nonlocal t, n
    for i in range(n, 2 * n):
        t[i] = (a[i - n], i - n)
    for i in range(n - 1, 0, -1):
        x = [t[2 * i], t[2 * i + 1]]
        x.sort(key=lambda x: x[0])
        t[i] = x[1]


def update(idx, value):
    nonlocal t, n
    idx = idx + n
    t[idx] = value

    while(idx > 1):
        idx = idx // 2
        x = [t[2 * idx], t[2 * idx + 1]]
        x.sort(key=lambda x: x[0])
        t[idx] = x[1]


n = int(input())
b = [-1] + list(numIN())
ans = [0] * (n + 1)
ans[1] = 0
ans[n] = b[1]
for i in range(2, n // 2 + 1):
    if b[i] <= b[i - 1]:
        ans[i] = ans[i - 1]
        ans[n - i + 1] = b[i] - ans[i]
    else:
        ans[n - i + 1] = ans[n - i + 2]
        ans[i] = b[i] - ans[n - i + 1]
print(' '.join([str(i) for i in ans[1:]]))
