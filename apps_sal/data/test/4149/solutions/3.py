import math
n = int(input())
b = list(map(int, input().split()))
N = 2750131
primes = {}
for i in range(2, N + 1):
    primes[i] = True
for i in range(2, math.floor(math.sqrt(N)) + 1):
    if primes[i]:
        for j in range(i * i, N + 1, i):
            primes[j] = False
nth_prime = []
for i in range(2, N + 1):
    if primes[i]:
        nth_prime.append(i)
len_nth = len(nth_prime)
primes_in_b = {}
non_primes_in_b = {}
divisors = {}
for number in b:
    if primes[number]:
        primes_in_b[number] = primes_in_b.get(number, 0) + 1
    else:
        non_primes_in_b[number] = non_primes_in_b.get(number, 0) + 1
        if divisors.get(number, 0) == 0:
            for prime in nth_prime:
                if number % prime == 0:
                    divisors[number] = number // prime
                    break
for number in sorted(non_primes_in_b.keys(), reverse=True):
    if primes[divisors[number]]:
        for i in range(non_primes_in_b[number]):
            primes_in_b[divisors[number]] -= 1
    else:
        for i in range(non_primes_in_b[number]):
            non_primes_in_b[divisors[number]] -= 1
for number in sorted(primes_in_b.keys()):
    for i in range(primes_in_b[number]):
        primes_in_b[nth_prime[number - 1]] -= 1
result = []
for number in primes_in_b:
    for i in range(primes_in_b[number]):
        result.append(number)
for number in non_primes_in_b:
    for i in range(non_primes_in_b[number]):
        result.append(number)
print(*result, sep=' ')
