q = 998244353

n, k = map(int, input().split())

lr = [list(map(int, input().split())) for _ in range(k)]

dp = [0] * (n + 1)
dpsum = [0] * (n + 1)


dp[1] = 1
dpsum[1] = 1

for i in range(2, n + 1):
    for l, r in lr:
        li = i - r
        ri = i - l
        if ri < 1: continue
        li = max(li, 1)
        dp[i] += (dpsum[ri] - dpsum[li - 1])
        dp[i] %= q
    dpsum[i] = dp[i] + dpsum[i - 1]
    dpsum[i] %= q

print(dp[n])
