
n = int(input())
r1 = list(map(int,input().split()))
r2 = list(map(int,input().split()))

# [i][0] sum when choosing r1 in pos
# [i][1] sum when choosing r2 in pos
# [i][2] sum when choosing nothing in pos
dp = [[0,0,0] for _ in range(n)] 
dp[0] = [r1[0],r2[0],0]
for i in range(1,n):
    last = dp[i-1]
    dp[i][0] = max(last[1], last[2]) + r1[i]
    dp[i][1] = max(last[0], last[2]) + r2[i]
    dp[i][2] = max(last[0], last[1])

print(max(dp[n-1]))

