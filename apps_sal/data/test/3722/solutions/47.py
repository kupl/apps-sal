MOD=10**9+7
a=['AAAA','BBBB','AAAB','AABA','AABB','ABAB','ABBB','BBAB']
b=['ABAA','BABA','BABB','BBAA']
c=['ABBA','BAAA','BAAB','BBBA']

N=int(input())
c=''.join([input() for _ in range(4)])

if c in a or N==2:
    print(1)
elif c in b:
    print(pow(2,N-3,MOD))
else:
    dp=[0]*N
    dp[0],dp[1]=1,1
    for i in range(2,N):
        dp[i]=(dp[i-1]+dp[i-2])%MOD
    print(dp[N-2])
