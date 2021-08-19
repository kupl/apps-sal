MOD = 10 ** 9 + 7
(n, k) = map(int, input().split())
cnt = [0] * (k + 1)
for i in range(1, k + 1):
    cnt[i] = pow(k // i, n, MOD)
dp = [0] * (k + 1)
for i in reversed(range(1, k + 1)):
    if not cnt[i]:
        continue
    tmp = cnt[i]
    for j in range(2, k + 1):
        if k < i * j:
            break
        tmp -= dp[i * j]
        tmp %= MOD
    dp[i] = tmp
ans = 0
for i in range(1, k + 1):
    ans += i * dp[i]
    ans %= MOD
print(ans)
