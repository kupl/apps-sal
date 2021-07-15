n, x  = map(int, input().split())
a = list(map(int, input().split()))
dp = [10**9 for i in range(max(a)+1)]
for i in range(n):
    if(dp[a[i]] == 0):
        print(0)
        return
    dp[a[i]] = 0
j= len(dp)-1

ans = 10**9
while j >=0:
    if dp[j] != 10**9:
        if(dp[j&x] != 10**9 and j !=j&x):
            ans = min(ans, dp[j&x] + dp[j]+1)
        dp[j&x] = min(dp[j&x], dp[j]+1)
    j-=1
if(ans==10**9):
    print(-1)
    return
print(ans)
