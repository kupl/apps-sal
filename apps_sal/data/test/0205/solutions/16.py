from sys import setrecursionlimit, stderr
from functools import reduce
from itertools import *
from collections import defaultdict, Counter
from bisect import bisect

setrecursionlimit(10**7)


def read():
    return int(input())


def reads():
    return [int(x) for x in input().split()]


def primes(n):
    sieve = [True] * (n // 2)
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [2 * i + 1 for i in range(1, n // 2) if sieve[i]]


PRIMES = primes(10**6 + 10)


def pfact(x):
    res = Counter()
    while x > 1:
        for p in PRIMES:
            if p >= x**0.5 + 1:
                res[x] += 1
                x = 1
                break
            if x % p == 0:
                res[p] += 1
                x //= p
                break
    return res


n, b = reads()
pb = pfact(b)

ans = 1 << 63
for p, e in list(pb.items()):
    k = sum(n // (p ** i) for i in takewhile(lambda i: p ** i <= n, count(1)))
    ans = min(k // e, ans)
print(ans)
