n, m = map(int, input().split())
a = list(map(int, input().split()))

match_num = {1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}

dp = [-1] * (n+10)
dp[0] = 0

for i in range(n):
    for j in range(m):
        nxt = match_num[a[j]]
        if dp[i]>=0:
            dp[i+nxt] = max(dp[i+nxt], dp[i]*10 + a[j])
print(dp[n])
