MOD = 10 ** 9 + 7
(N, K) = map(int, input().split())
ans = 0
for k in range(K, N + 2):
    ans += (N - k + 1) * k + 1
    ans %= MOD
print(ans)
