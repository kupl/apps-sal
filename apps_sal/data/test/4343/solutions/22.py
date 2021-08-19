import sys
from bisect import bisect_left, bisect_right
from collections import deque, Counter
from math import gcd, sqrt, factorial, ceil, log
from itertools import permutations
inf = float('inf')
mod = 1000000007
mini = 1000000007


def fact(n):
    if n == 0:
        return 1
    p = 1
    d = 10 ** 9 + 7
    for i in range(1, n + 1):
        p = p * i
        p = p % d
    return p


def ncr(n, r):
    d = 10 ** 9 + 7
    num = fact(n)
    den = fact(r) * fact(n - r) % d
    den = pow(den, d - 2, d)
    return num * den % d


def sieve(n):
    prime = [True for i in range(n + 1)]
    lst = [0] * (n + 1)
    p = 2
    while p * p <= n:
        if prime[p]:
            lst[p] = p
            for i in range(p * p, n + 1, p):
                if prime[i] == True:
                    prime[i] = False
                    lst[i] = p
        p = p + 1
    for i in range(1, n + 1):
        if lst[i] == 0:
            lst[i] = i
    mylist = [0] * (n + 1)
    for i in range(2, n + 1):
        mylist[lst[i]] = mylist[lst[i]] + 1
    return mylist


def binary(number):
    result = 0
    while number:
        result = result + 1
        number = number & number - 1
    return result


def calculate_factors(n):
    hh = [1] * (n + 1)
    p = 2
    while p * p < n:
        if hh[p] == 1:
            for i in range(p * 2, n, p):
                hh[i] = 0
        p += 1
    total = 1
    for p in range(2, n + 1):
        if hh[p] == 1:
            count = 0
            if n % p == 0:
                while n % p == 0:
                    n = int(n / p)
                    count += 1
                total *= count + 1
    return total


def prime_factors(n):
    i = 2
    factors = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    if len(factors) == 2:
        return True
    else:
        return False


def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def get_array():
    return list(map(int, sys.stdin.readline().strip().split()))


def get_ints():
    return map(int, sys.stdin.readline().strip().split())


def input():
    return sys.stdin.readline().strip()


n = int(input())
A = [ord(c) - 97 for c in input()]
B = [ord(c) - 97 for c in input()]
C = [a + b for (a, b) in zip(A, B)]
D = [0] * n
for i in range(n):
    if C[i] & 1:
        D[i + 1] += 13
    D[i] += C[i] // 2
for i in reversed(range(n)):
    while D[i] >= 26:
        D[i - 1] += 1
        D[i] -= 26
print(*[chr(d + 97) for d in D], sep='')
