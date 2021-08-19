#!/usr/bin/env python
from math import sqrt
from collections import Counter


def gen_primes(X):
    D = [0] * (X + 1)
    is_prime = [True for _ in range(0, X + 1)]
    is_prime[0] = False
    is_prime[1] = False
    primes = []
    for n in range(2, int(sqrt(X)) + 1):
        if is_prime[n]:
            primes.append(n)
            j = n * 2
            D[n] = n
            while j <= X:
                is_prime[j] = False
                if D[j] == 0:
                    D[j] = n
                j += n
    for n in range(int(sqrt(X)), X + 1):
        if is_prime[n]:
            D[n] = n
            primes.append(n)
    return primes, D


def solve(A):
    N = len(A)
    primes, D = gen_primes(10**6)
    C = [0] * (primes[-1] + 1)

    for a in A:
        a_ = a
        while a > 1:
            d = D[a]
            while a % d == 0:
                a //= d
            C[d] += 1

    M = max(C)
    if M <= 1:
        print("pairwise coprime")
    elif M != N:
        print("setwise coprime")
    else:
        print("not coprime")


#solve([x for x in range(1, 10**6+1)])
N = int(input())
A = [int(x) for x in input().split()]
solve(A)
