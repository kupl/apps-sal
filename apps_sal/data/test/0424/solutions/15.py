n = int(input())
is_prime = [True] * n
for i in range(2, n):
    if is_prime[i]:
        for j in range(i * i, n, i):
            is_prime[j] = False
primes = [i for i in range(2, n) if is_prime[i]]
m = n - 1
for p in primes:
    if n % p == 0:
        m = n - p
answer = m + 1
for p in primes:
    if p > m:
        break
    d = m - m % p
    if d + p <= n:
        answer = min(answer, d + 1)
print(answer)
