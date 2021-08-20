(n, m) = map(int, input().split())
MOD = 10 ** 9 + 7
ans = 1
ans *= pow(2, m, MOD) - 1
ans %= MOD
ans = pow(ans, n, MOD)
print(ans % MOD)
