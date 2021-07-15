n, k = list(map(int, input().split()))
mod = 998244353
arr = []
for i in range(k):
    arr.append(list(map(int, input().split())))
arr.sort()
dp = [0] * (n+1)
dp[1] = 1
presum = [0] * 10
for i in range(2, n+1):
    for j in range(k):
        presumj = presum[j]
        if i - arr[j][0] >= 1:
            presumj += dp[i - arr[j][0]]
        if i - arr[j][1] -1 >= 1:
            presumj -= dp[i - arr[j][1] -1]
        presumj %= mod
        presum[j] = presumj
        dp[i] += presumj
        dp[i] %= mod
print(dp[n])
