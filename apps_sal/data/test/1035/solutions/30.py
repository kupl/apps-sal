import math
(A, B) = [int(x) for x in input().split()]


def prime_factorization(n):
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


C = math.gcd(A, B)
print(len(set(prime_factorization(C))) + 1)
