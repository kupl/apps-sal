from math import gcd


def division(n):
    if n < 2:
        return [1]
    prime_factors = [1]
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            prime_factors.append(i)
            n //= i
    if n > 1:
        prime_factors.append(n)
    return prime_factors


(a, b) = map(int, input().split())
d = set(division(gcd(a, b)))
print(len(d))
