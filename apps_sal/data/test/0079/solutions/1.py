MOD = 10 ** 9 + 7
m = int(input())
f = [0] * (m + 1)
ans = 1
for i in range(m, 1, -1):
    p = m // i * pow(m, MOD - 2, MOD)
    f[i] = p * pow(1 - p, MOD - 2, MOD) % MOD
    for j in range(2 * i, m + 1, i):
        f[i] = (f[i] - f[j]) % MOD
    ans += f[i]
print(ans % MOD)
