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
    while i * i <= n:
        if n % i:
            i += 2
        else:
            n //= i
            prime.append(i)
            while n % i == 0:
                n //= i
    if n > 1:
        prime.append(n)
    return prime


print(len(prime_factorization(gcd)) + 1)
