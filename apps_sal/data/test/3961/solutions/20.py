def R():
    return map(int, input().split())


n = int(input())
mod = 1000000007
arr = [x - 1 for x in R()]
dp = [0] * (n + 1)
sdp = [0] * (n + 1)
dp[0] = sdp[0] = 2
for i in range(1, len(arr)):
    dp[i] = (2 + sdp[i - 1] - sdp[arr[i] - 1]) % mod
    sdp[i] = (sdp[i - 1] + dp[i]) % mod
print(sdp[n - 1])
