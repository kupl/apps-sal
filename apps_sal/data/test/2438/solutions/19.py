import sys
import itertools
import math
import collections
from collections import Counter


def pow(x, y, mod):
    r = 1
    x = x % mod
    while y > 0:
        if y & 1:
            r = (r * x) % mod
        y = y >> 1
        x = (x * x) % mod
    return r


def sieve(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = prime[1] = False
    r = [p for p in range(n + 1) if prime[p]]
    return r


def divs(n, start=1):
    r = []
    for i in range(start, int(math.sqrt(n) + 1)):
        if (n % i == 0):
            if (n / i == i):
                r.append(i)
            else:
                r.extend([i, n // i])
    return r


def cdiv(n, k): return n // k + (n % k != 0)
def ii(): return int(input())
def mi(): return list(map(int, input().split()))
def li(): return list(map(int, input().split()))
def lcm(a, b): return abs(a * b) // math.gcd(a, b)
def prr(a, sep=' '): print(sep.join(map(str, a)))
def dd(): return collections.defaultdict(int)


n = ii()
s = input()
used = [set() for i in range(n)]
i = 0
res = 0
while i < n - 1:
    if s[i] != s[i + 1]:
        j = i + 1
        while j < n and s[j] != s[i]:
            used[i].add(j)
            res += 1
            j += 1
        i = j - 1
        continue
    i += 1

i = n - 1
while i > 1:
    if s[i] != s[i - 1]:
        j = i - 1
        while j >= 0 and s[j] != s[i]:
            if i not in used[j]:
                res += 1
            j -= 1
        i = j + 1
        continue
    i -= 1

print((n * (n - 1)) // 2 - res)
