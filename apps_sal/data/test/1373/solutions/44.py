(N, K) = map(int, input().split())
MOD = 10 ** 9 + 7
ans = 1
for i in range(K, N + 1):
    ans += i * (2 * N - i + 1) // 2 % MOD - i * (i - 1) // 2 % MOD + 1
    ans %= MOD
print(ans)
