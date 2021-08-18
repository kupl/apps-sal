import sys
from collections import Counter
from bisect import bisect_left


def Sieve(l):
    primes = [0] * 2 + [1] * l
    for i in range(l):
        if primes[i]:
            for j in range(i * i, l, i):
                primes[j] = 0
    primes = [k for k in range(l) if primes[k]]
    return primes


def index(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError


n = int(input())
a = sorted(list(map(int, sys.stdin.readline().split())))
b = Counter(a)
actual = Counter()
l = -1
prime = Sieve(a[-1] + 1)
while l != -2 * n:
    mx = a[l]
    if b[mx] > 0:
        try:
            second = index(prime, mx) + 1
            actual[second] = actual[second] + b[mx]
        except:
            i = 0
            while mx % prime[i] != 0:
                i = i + 1
            second = mx // prime[i]
            actual[mx] = actual[mx] + b[mx]
        l = l - b[mx]
        b[second] = b[second] - b[mx]
        b[mx] = 0
    else:
        l = l - 1
print(*actual.elements(), sep=' ')
