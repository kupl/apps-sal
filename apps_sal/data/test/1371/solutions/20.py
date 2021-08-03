base = 10**9 + 7


def comb_mod(n, r, MOD=base):
    if n < 0 or r < 0 or n < r:
        return 0

    factrial = [1] * (n + 1)
    for k in range(1, n + 1):
        factrial[k] = (factrial[k - 1] * k) % MOD

    fact_inv = [1] * (n + 1)
    fact_inv[n] = pow(factrial[n], MOD - 2, MOD)
    for k in range(n - 1, -1, -1):
        fact_inv[k] = (fact_inv[k + 1] * (k + 1)) % MOD

    return (factrial[n] * fact_inv[r] * fact_inv[n - r]) % MOD


s = int(input())
out = 0
n = s // 3
for i in range(1, n + 1):
    out += comb_mod(s - 3 * i + i - 1, i - 1)
print(out % base)
