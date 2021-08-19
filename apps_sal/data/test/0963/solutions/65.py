MOD = 998244353
(N, K) = map(int, input().split())
S = []
for _ in range(K):
    s = list(map(int, input().split()))
    S.append(s)
dp = [0] * N
dp[0] = 1
ds = [1] * N
for i in range(1, N):
    for s in S:
        if i - s[0] < 0:
            continue
        if i - s[1] - 1 < 0:
            dp[i] += ds[i - s[0]] % MOD
        else:
            dp[i] += (ds[i - s[0]] - ds[i - s[1] - 1]) % MOD
    ds[i] = ds[i - 1] + dp[i] % MOD
print(dp[-1] % MOD)
