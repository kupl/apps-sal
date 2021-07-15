from sys import stdin
ip = lambda :[int(w) for w in stdin.readline().split()]

n,m,k = [int(w) for w in stdin.readline().split()]
sp = 2 if k == 1 else 0
dp = [[1]*(m+1) for j in range(n+1)]
for j in range(k):
    x,y,t,f = [int(w) for w in stdin.readline().split()]
    dp[x][y] = 0
    for i in range(1,n+1):
        reach = i + y -2 - t - abs(x-i) +sp
        if reach > 0 and reach % f == 0:
            dp[i][y] = 0
    for i in range(1,m+1):
        reach = i + x -2 - t - abs(y-i) +sp
        if reach > 0 and reach % f == 0:
            dp[x][i] = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        cur,left,up = dp[i][j],dp[i][j-1],dp[i-1][j]
        dp[i][j] = cur*left or cur*up

if dp[-1][-1]:
    print("YES")
    print(n+m-2)
else:
    print("NO")
