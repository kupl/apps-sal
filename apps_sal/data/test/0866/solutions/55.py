X, Y = list(map(int, input().split()))
mod = 10**9 + 7


def permute(n, m):
    ret = 1
    while n >= m:
        ret *= n
        # ret %= mod
        n -= 1

    return ret


def count_combinations(n, m):
    fact = [1] * (n + 1)
    inv = [i for i in range(n + 1)]
    fact_inv = [1] * (n + 1)

    for i in range(2, n + 1):
        fact[i] = fact[i - 1] * i % mod
        inv[i] = (-inv[mod % i] * (mod // i)) % mod
        # inv[i] = mod - inv[mod % i] * (mod // i) % mod
        fact_inv[i] = fact_inv[i - 1] * inv[i] % mod

    ret = (fact[n] * fact_inv[m] * fact_inv[n - m]) % mod

    return ret


def count_comb2(n, m):
    fact = [1, 1]  # fact[n] = (n! mod p)
    factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
    inv = [0, 1]  # factinv 計算用

    for i in range(2, n + 1):
        fact.append((fact[-1] * i) % mod)
        inv.append((-inv[mod % i] * (mod // i)) % mod)
        factinv.append((factinv[-1] * inv[-1]) % mod)

    if (m < 0) or (n < m):
        return 0
    m = min(m, n - m)
    return fact[n] * factinv[m] * factinv[n - m] % mod


ret = 0
if (X + Y) % 3 == 0:
    m = (2 * X - Y) // 3
    n = (2 * Y - X) // 3

    if m >= 0 and n >= 0:
        ret = count_combinations(n + m, m)
        # ret = count_comb2(n+m, m)

print(ret)
