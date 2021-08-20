from collections import Counter


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


MOD = 10 ** 9 + 7
(n, m) = map(int, input().split())
c = Counter(prime_factorize(m))
cv = list(c.values())
ans = 1
for i in cv:
    for j in range(i):
        ans *= i + n - 1 - j
        ans %= MOD
        ans *= pow(1 + j, MOD - 2, MOD)
        ans %= MOD
print(ans)
