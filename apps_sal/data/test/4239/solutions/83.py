n = int(input())
a_6 = [int(6**i) for i in range(1,10) if 6**i <= 10**5]
a_9 = [int(9**i) for i in range(1,10) if 9**i <= 10**5]
a = [1]
for i in a_6:
    a.append(i)
for i in a_9:
    a.append(i)
a.sort(reverse = True)
dp = [i for i in range(n+1)]
dp[0] = 0
for i in range(n+1):
    for j in a:
        if i+j <= n:
            dp[i+j] = min(dp[i+j],dp[i]+1)
print(dp[n])
