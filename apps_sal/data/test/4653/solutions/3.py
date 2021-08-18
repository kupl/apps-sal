import sys
import collections
from collections import Counter
import itertools
import math
import timeit


def sieve(n):
    if n < 2:
        return list()
    prime = [True for _ in range(n + 1)]
    p = 3
    while p * p <= n:
        if prime[p]:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 2
    r = [2]
    for p in range(3, n + 1, 2):
        if prime[p]:
            r.append(p)
    return r


def divs(n, start=1):
    divisors = []
    for i in range(start, int(math.sqrt(n) + 1)):
        if n % i == 0:
            if n / i == i:
                divisors.append(i)
            else:
                divisors.extend([i, n // i])
    return divisors


def divn(n, primes):
    divs_number = 1
    for i in primes:
        if n == 1:
            return divs_number
        t = 1
        while n % i == 0:
            t += 1
            n //= i
        divs_number *= t


def flin(d, x, default=-1):
    left = right = -1
    for i in range(len(d)):
        if d[i] == x:
            if left == -1:
                left = i
            right = i
    if left == -1:
        return (default, default)
    else:
        return (left, right)


def ceil(n, k): return n // k + (n % k != 0)
def ii(): return int(input())
def mi(): return list(map(int, input().split()))
def li(): return list(map(int, input().split()))
def lcm(a, b): return abs(a * b) // math.gcd(a, b)
def prr(a, sep=' '): print(sep.join(map(str, a)))
def dd(): return collections.defaultdict(int)
def ddl(): return collections.defaultdict(list)


t = ii()
for _ in range(t):
    n, k = mi()
    q = n // k
    print(min(n, q * k + (k // 2)))
