n, m, k = map(int, input().split())
MOD = 1000000009
x = m - (n // k * (k - 1) + (n % k))
if (x <= 0):
    print(m % MOD)
    return
print(((m - x) + ((pow(2, x + 1, MOD) + 2 * MOD) - 2) * k - x * (k - 1)) % MOD)
