N, M, K = list(map(int, input().split()))
MOD = 998244353
ans = 0
comb = 1
for k in range(K + 1):
    ans += M * comb * pow(M - 1, N - k - 1, MOD)
    ans %= MOD
    comb *= (N - k - 1) * pow(k + 1, MOD - 2, MOD)
    comb %= MOD
print(ans)
