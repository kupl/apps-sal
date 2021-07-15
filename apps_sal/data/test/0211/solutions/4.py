MOD = 1000000009
n, m, k = list(map(int, input().split()))
x = m - (n // k * (k - 1) + n % k)

if x <= 0:
    print(m)
else:
    print(((m - x) + (pow(2, x + 1, MOD) - 2) * k - x * (k - 1)) % MOD)

