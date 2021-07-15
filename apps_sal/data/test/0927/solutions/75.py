nim,mike = map(int,input().split())
array = list(map(int,input().split()))

dp = [-1 for i in range(nim+10)]
l = [0,2,5,5,4,5,6,3,7,6]
dp[0] = 0
for i in range(nim-1):
    for s in array:
        if dp[i] == -1 and i!=0:
            continue
        if dp[i + l[s]] < dp[i]*10+s:
            dp[i + l[s]] = dp[i]*10+s
print(dp[nim])
