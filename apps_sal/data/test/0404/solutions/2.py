def to_prime(n):
    i = 2
    primes = []
    while (i * i <= n):
        if (n % i == 0):
            amount = 0
            while (n % i == 0):
                amount += 1
                n //= i
            primes.append((i, amount))
        i += 1
    if (n != 1):
        primes.append((n, 1))
    return primes

n = int(input())

primes = to_prime(n)
result = 1
for p, k in primes:
    result *= k + 1
print(result)

