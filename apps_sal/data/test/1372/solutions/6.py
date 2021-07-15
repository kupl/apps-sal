h,n = list(map(int,input().split()))

ab = [list(map(int,input().split())) for i in range(n)]
ma = max(a for a,b in ab)


dp = [10**10]*(h+ma+1)
dp[0] = 0

for i in range(1,h+ma+1):
    dp[i] = min(dp[i-a]+b for a,b in ab)

print((min(dp[h:])))

