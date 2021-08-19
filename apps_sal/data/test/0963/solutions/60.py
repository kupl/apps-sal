(N, K) = list(map(int, input().split()))
S = [list(map(int, input().split())) for _ in range(K)]
dp = [0 for _ in range(N + 1)]
S.sort()
dp[0] = 0
for i in range(1, S[0][0] + 1):
    dp[i] = 1
for i in range(S[0][0] + 1, N + 1):
    rui = 0
    for s in S:
        if i - s[0] > 0:
            end = max([i - s[1], 0])
            rui += (dp[i - s[0]] - dp[end - 1]) % 998244353
    dp[i] = (dp[i - 1] + rui) % 998244353
print((dp[N] - dp[N - 1]) % 998244353)
