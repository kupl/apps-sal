from collections import defaultdict

N = int(input())
*A, = list(map(int, input().split()))
INF = 10**20
dp = defaultdict(lambda :-INF)
dp[(0,0,0)] = 0

for i in range(1, N+1):
    for j in range(i//2-1, i//2+2):
        dp[1,i,j] = dp[0,i-1,j-1]+A[i-1]
        dp[0,i,j] = max(dp[1,i-1,j], dp[0,i-1,j])

ans = max(dp[1,N,N//2], dp[0,N,N//2])
print(ans)

