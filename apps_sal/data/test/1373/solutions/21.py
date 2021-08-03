N, K = map(int, input().split())
mod = 10**9 + 7
ans = 0
for i in range(K, N + 2):
    ans += i * (N - i + 1) % mod + 1
    ans %= mod
print(ans)
