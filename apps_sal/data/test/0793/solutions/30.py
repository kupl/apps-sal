N, M = map(int, input().split())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
dp = [1] * (M + 1)
acc = [0] * (M)
MOD = 10 ** 9 + 7
for s in S:
    ndp = [1]
    for i, t in enumerate(T):
        if s == t:
            ndp.append(ndp[-1] + dp[i + 1])
            acc[i] = dp[i + 1]
        else:
            ndp.append(ndp[-1] + acc[i])
    dp = ndp
print(dp[-1] % MOD)
