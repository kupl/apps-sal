import math
a, b = map(int, input().split())
gcd = math.gcd(a, b)


def prime_factorization(n):
    i = 2
    prime = []
    if n % i == 0:
        n //= i
        prime.append(2)
        while n % i == 0:
            n //= i
    i += 1
    k = int(n**0.5) + 1
    for j in range(i, k + 1, 2):
        if n % j == 0:
            n //= j
            prime.append(j)
            while n % j == 0:
                n //= j
    if n > 1:
        prime.append(n)
    return prime


print(len(prime_factorization(gcd)) + 1)
