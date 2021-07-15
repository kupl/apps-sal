MOD = 1000000007
ii = lambda: int(input())
si = lambda: input()
dgl = lambda: list(map(int, input()))
f = lambda: list(map(int, input().split()))
il = lambda: list(map(int, input().split()))
ls = lambda: list(input())
s=si()
n=len(s)
dp=[0]*(n+2)
dp[0]=1
dp[1]=1 if not s[0] in ['m','w'] else 0
for i in range(2,n+1):
    if s[i-1] in ['m','w']:
        print(0);return
    dp[i]=dp[i-1]
    if s[i-1]=='n' or s[i-1]=='u':
        if s[i-2]==s[i-1]:
            dp[i]+=dp[i-2]
            dp[i]%=MOD
print(dp[n])


