import math
a, b = list(map(int, input().split()))
gcd = math.gcd(a, b)


def prime_factorization(n):
    i = 2
    prime = []
    while i * i <= n and n > 1:
        if n % i:
            i += 1
        else:
            n //= i
            prime.append(i)
            while n % i == 0:
                n //= i
    if n > 1:
        prime.append(n)
    return prime


print((len(prime_factorization(gcd)) + 1))
# print(prime_factorization(gcd))
