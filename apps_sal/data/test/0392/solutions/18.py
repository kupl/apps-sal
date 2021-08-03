'''
Created on Oct 15, 2015

@author: Ismael
'''
from collections import Counter
n = int(input())


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def product(l):
    p = 1
    for i in l:
        p *= i
    return p


print(product(Counter(prime_factors(n)).keys()))
