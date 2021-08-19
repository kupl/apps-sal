mod = 10 ** 9 + 7
(N, k) = map(int, input().split())
ans = 0
for j in range(k, N + 2):
    ans += (N - j + 1) * j
    ans += 1
    ans %= mod
print(ans % mod)
