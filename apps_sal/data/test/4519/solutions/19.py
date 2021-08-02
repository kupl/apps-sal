import sys
import itertools
import math
import collections
from collections import Counter

#########################
# imgur.com/Pkt7iIf.png #
#########################


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


def ceil(n, k): return n // k + (n % k != 0)
def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(map(int, input().split()))
def lcm(a, b): return abs(a * b) // math.gcd(a, b)
def prr(a, sep=' '): print(sep.join(map(str, a)))
def dd(): return collections.defaultdict(int)


t = ii()
for _ in range(t):
    n, k = mi()
    s = input()
    state = []
    pos = 0
    for i in range(n):
        if s[i] == '0':
            if k != 0 and i - pos <= k:
                state.append(pos)
                k -= (i - pos)
                pos += 1
            elif k != 0:
                state.append(i - k)
                k = 0
            else:
                state.append(i)
    res = [1] * n
    for i in state:
        res[i] = 0
    prr(res, '')
