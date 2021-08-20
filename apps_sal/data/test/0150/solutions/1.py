def rwh_primes(n):
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


primes = rwh_primes(44722)


def isPrime(z):
    if z < 44722:
        return z in primes
    else:
        for p in primes:
            if z % p == 0:
                return False
        return True


n = int(input())
if n & 1:
    if isPrime(n):
        print(1)
    elif isPrime(n - 2):
        print(2)
    else:
        print(3)
elif n == 2:
    print(1)
else:
    print(2)
