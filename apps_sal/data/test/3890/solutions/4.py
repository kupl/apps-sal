MOD = 10 ** 9 + 7
n, k = map(int, input().split())
ans = pow(n - k, n - k, MOD) * pow(k, k - 1, MOD)
print(ans % MOD)
