n,k=map(int,input().split())
s=input()
s=[ord(c)-ord('a') for c in s]
dp=[[[0]*26 for i in range(n+1)]for i in range(n)]
dp[0][1][s[0]]=1
sm=None

for i in range(1,n):
    c=s[i]
    for cc in range(26):
        dp[i][1][cc]=dp[i-1][1][cc]
    dp[i][1][c]=1
    for j in reversed(range(2,n+1)):
        for cc in range(26):
            if cc!=c:
                dp[i][j][cc]=dp[i-1][j][cc]
            else:
                tm=0
                for t in range(26):
                    tm+=dp[i-1][j-1][t]
                dp[i][j][cc]=tm
# print(dp[-1][-1])
def get(x):
    if x==0:
        return 1
    ans=0
    for i in range(26):
        ans+=dp[-1][x][i]
    return ans
cnt=0
cost=0
for re in reversed(range(n+1)):
    x=get(re)
    if x+cnt>=k:
        cost+=(n-re)*(k-cnt)
        cnt=k
        break
    else:
        cost+=(n-re)*x
        cnt+=x
if cnt<k:
    print(-1)
else:
    print(cost)
