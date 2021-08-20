def prime_factor(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            while n % i == 0:
                n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors


def mebius(n):
    res = {}
    primes = prime_factor(n)
    m = len(primes)
    for i in range(1 << m):
        mu = 1
        d = 1
        for j in range(m):
            if i >> j & 1:
                mu *= -1
                d *= primes[j]
        res[d] = mu
    return res


mod = 10 ** 9 + 7
(N, K) = list(map(int, input().split()))
div = divisors(N)
ans = 0
for x in div:
    div2 = divisors(x)
    mu = mebius(x)
    cnt = 0
    for y in list(mu.keys()):
        cnt += pow(K, (x // y + 1) // 2, mod) * mu[y]
    if x % 2 == 0:
        cnt *= pow(2, mod - 2, mod)
    ans += x * cnt
    ans %= mod
print(ans)
