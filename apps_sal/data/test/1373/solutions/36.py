MOD = 10 ** 9 + 7
(N, K) = map(int, input().split())
ans = 0
ans += N - K + 2
ans += (N + 1) * (N + 1 + K) * (N - K + 2) // 2
ans %= MOD
ans -= (N + 1) * (N + 2) * (2 * N + 3) // 6
ans %= MOD
ans += K * (K - 1) * (2 * K - 1) // 6
ans %= MOD
print(ans)
