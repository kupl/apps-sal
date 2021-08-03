from bisect import bisect_right as br
from bisect import bisect_left as bl
from collections import defaultdict
from itertools import combinations
import sys
import math
MAX = sys.maxsize
MAXN = 10**6 + 10
MOD = 998244353


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


def dis(a, b, k):
    ans = 0
    for i in range(k):
        ans += abs(a[i] - b[i])
    return ans


def cal(n, k):
    res = 1
    c = [0] * (k + 1)
    c[0] = 1
    for i in range(1, n + 1):
        for j in range(min(i, k), 0, -1):
            c[j] = (c[j] + c[j - 1]) % MOD
    return c[k]


for _ in range(int(input())):
    n, k = numIN()
    s = ''
    for i in range(1, k + 1):
        s += chr(i + 96)
    for i in range(k, n):
        s += s[i - k]
    print(s)
