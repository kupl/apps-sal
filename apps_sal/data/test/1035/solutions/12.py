def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
a, b = map(int, input().split())
n = gcd(a, b)
primes = []
MAX = 10 ** 6 + 10
is_prime = [False] * 2 + [True] * (MAX - 2)
for i in range(2, MAX):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * i, MAX, i):
            is_prime[j] = False
cnt = 1
for p in primes:
    if n % p == 0:
        cnt += 1
        while n % p == 0:
            n /= p
if n != 1:
    cnt += 1
print(cnt)
