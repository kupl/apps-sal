h,n = map(int,input().split())

ab_input = [list(map(int,input().split())) for i in range(n)]
max_d = max(a for a,b in ab_input)
#配るdp
dp =[0]*(h+max_d)
for i in range(1,h+max_d):
    dp[i]=min(dp[i-a]+b for a,b in ab_input)
print(dp[h])
