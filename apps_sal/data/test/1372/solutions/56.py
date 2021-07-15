H,N = map(int,input().split())
ls = []
maxA = 0
for i in range(N):
    A,B = map(int,input().split())
    ls.append([A,B])
    maxA = max(maxA,A)
dp = [0 for i in range(H+maxA+1)]
for i in range(1,H+maxA+1):
    dp[i] = min(dp[i - j[0]] + j[1] for j in ls )
print(dp[H])
