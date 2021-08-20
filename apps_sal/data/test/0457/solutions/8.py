def prime_divs(n):
    divs = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            divs.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        divs.append(n)
    return divs


def pwrmod(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return (pwrmod(a, n // 2) % MOD) ** 2
    return pwrmod(a, n - 1) * a % MOD


(x, n) = list(map(int, input().split()))
MOD = 10 ** 9 + 7
ans = 1
for d in prime_divs(x):
    pwrsum = 0
    pwr = d
    while pwr <= n:
        pwrsum += n // pwr
        pwr *= d
    ans = ans * pwrmod(d, pwrsum) % MOD
print(ans)
