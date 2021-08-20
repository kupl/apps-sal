(N, K) = list(map(int, input().split()))
ans = 0
mod = 10 ** 9 + 7
for k in range(K, N + 2):
    ans += max((N - k + 1) * k + 1, 0)
print(ans % mod)
