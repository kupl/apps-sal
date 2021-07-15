N,M,Q = map(int,input().split())
line = [tuple(map(int,input().split())) for i in range(M)]
query = [tuple(map(int,input().split())) for i in range(Q)]
dp = [[0 for i in range(N+1)] for i in range(N+1)]
for l in line:
    dp[l[0]][l[1]] += 1
for i in range(N):
    for j in range(N):
        dp[i+1][j+1] += dp[i+1][j]
for i in range(N):
    for j in range(N):
        dp[i+1][j+1] += dp[i][j+1]
for p,q in query:
    print(dp[q][q]-dp[q][p-1]-dp[p-1][q]+dp[p-1][p-1])
