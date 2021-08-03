# import math
# N=10010
# def solve(ar):
# 	dp=[0 for i in range(N+20)]
# 	for i in ar:
# 		x=math.sqrt(i)
# 		for j in range(2,x+1):
# 			if(i%j==0):
# 				dp[i]=max(dp[i],max(dp[j]+1,dp[i//j]+1))
#         for j in range(2,x+1):
#         	if(i%j==0):
#         		dp[j]=dp[i//j]=dp[i]
#     m=1
#     for i in range(1,10010):
#     	m=max(m,dp[i])
#     return m
import math
N = 100100


def solve(ar):
    n = len(ar)
    dp = [0 for i in range(N + 20)]
    for a in ar:
        x = math.sqrt(a)
        dp[a] = 1
        for j in range(2, a):
            if(j * j <= a):
                if(a % j == 0):
                    dp[a] = max(dp[a], max(dp[a // j] + 1, dp[j] + 1))
            else:
                break
        for j in range(2, a):
            if(j * j <= a):
                if(a % j == 0):
                    dp[j] = dp[a // j] = dp[a]
            else:
                break

    m = 1
    for x in range(1, 100100):
        m = max(m, dp[x])
    return m


n = int(input())
ar = list(map(int, input().split()))
x = solve(ar)
print(x)
