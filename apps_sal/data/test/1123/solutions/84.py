mod = 10 ** 9 + 7
(n, k) = map(int, input().split())
cnt = [0] * (k + 1)
for i in range(k, 0, -1):
    cnt[i] += pow(k // i, n, mod)
    for j in range(2, k // i + 1):
        cnt[i] -= cnt[i * j]
ans = 0
for i in range(1, k + 1):
    ans += i * cnt[i] % mod
    ans %= mod
print(ans)
