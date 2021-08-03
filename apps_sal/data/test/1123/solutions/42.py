N, K = list(map(int, input().split()))
MOD = 1_000_000_007
gcd_cnt = [0] * (K + 1)
for g in range(K, 0, -1):
    gcd_cnt[g] = pow(K // g, N, MOD)
    for g_mul in range(2, K // g + 1):
        gcd_cnt[g] -= gcd_cnt[g * g_mul]

ans = 0
for g, cnt in enumerate(gcd_cnt):
    ans += g * cnt % MOD
    ans %= MOD
print(ans)
