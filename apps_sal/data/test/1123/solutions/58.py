(n, k) = list(map(int, input().split()))
MOD = 1000000007
cnt = [0] * (k + 1)
for i in range(1, k + 1):
    cnt[i] = pow(k // i, n, MOD)
for i in range(k, 0, -1):
    j = i * 2
    while j <= k:
        cnt[i] = (MOD + cnt[i] - cnt[j]) % MOD
        j += i
ans = 0
for i in range(1, k + 1):
    ans = (ans + cnt[i] * i) % MOD
print(ans)
