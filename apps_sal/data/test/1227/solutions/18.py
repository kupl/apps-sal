S = input()
L = len(S)
K = int(input())

dp = [[[0, 0] for _ in range(K + 1)] for _ in range(L + 1)]
dp[0][0][0] = 1
for i, c in enumerate(S):
    c = int(c)
    for k in reversed(range(K + 1)):
        for d in range(10):
            nk = k + (d > 0)
            if nk > K: continue
            dp[i + 1][nk][1] += dp[i][k][1]
            if d > c: continue
            less = int(d < c)
            dp[i + 1][nk][less] += dp[i][k][0]
print(sum(dp[-1][-1]))
