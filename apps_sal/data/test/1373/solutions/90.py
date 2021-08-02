N, K = map(int, input().split())
ans = 0
bigint = 10**9 + 7
for k in range(K, N + 2):
    ans += N - k + 2 + (N - k + 1) * (k - 1)
    ans %= bigint
print(ans)
