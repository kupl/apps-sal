def getPrimes(n):
    primes = [0 for _ in range(n + 1)]
    for i in range(2, n + 1):
        if not primes[i]:
            for j in range(2 * i, n + 1, i):
                primes[j] = i
        primes[i] = i - primes[i] + 1
    return primes


x2 = int(input())
primes = getPrimes(x2)

res = x2
for i in range(primes[x2], x2 + 1):
    res = min(res, primes[i])

print(res)
