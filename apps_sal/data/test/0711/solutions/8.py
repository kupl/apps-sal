from collections import Counter

n, m = list(map(int, input().split()))

if m == 1:
    print(1)
else:

    MOD = pow(10, 9) + 7

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

    def make_fact_list(n, MOD):
        fact = [0] * (n + 1)
        inv = [0] * (n + 1)
        factinv = [0] * (n + 1)

        fact[0] = fact[1] = 1
        inv[1] = 1
        factinv[0] = factinv[1] = 1

        for i in range(2, n + 1):
            fact[i] = fact[i - 1] * i % MOD
            inv[i] = MOD - ((inv[MOD % i] * (MOD // i)) % MOD)
            factinv[i] = factinv[i - 1] * inv[i] % MOD

        return fact, factinv

    def cbn(n, k, MOD, fact=[], factinv=[]):
        if len(fact) == 0 and len(factinv) == 0:
            fact, factinv = make_fact_list(n, MOD)
        return fact[n] * factinv[n - k] * factinv[k] % MOD

    d = Counter(prime_factorize(m)).most_common()

    l = d[0][1] + n

    fact, factinv = make_fact_list(l, MOD)

    a = 1

    for k, v in d:
        a *= cbn(v + n - 1, v, MOD, fact=fact, factinv=factinv) % MOD

    print(a % MOD)
