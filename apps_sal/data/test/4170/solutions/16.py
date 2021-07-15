n = int(input())
H = list(map(int, input().split()))
dp = [0]*n
dp[0] = 1

if n == 1:
    print((0))
else:
    for i in range(1, n-1):
        if H[i] >= H[i+1]:
            dp[i] += dp[i-1]+1
        else:
            dp[i] = 0
    print((max(dp[1:])))
         

