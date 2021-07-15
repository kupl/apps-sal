from math import factorial

n = int(input())
f = factorial(n)

mod = 10 ** 9 + 7

def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

ans = 1
for p in primes(n):
    temp = 1
    while f % p == 0:
        temp += 1
        f //= p
    ans = (ans * temp) % mod
print(ans)
