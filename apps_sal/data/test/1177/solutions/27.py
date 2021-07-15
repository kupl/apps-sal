import sys

def input(): return sys.stdin.readline()[:-1]

#mod = 10**9+7
#w.sort(key=itemgetter(1),reversed=True)  #二個目の要素で降順並び替え

#N = int(input())
_, S = list(map(int, input().split()))
#L = [int(input()) for i in range(N)]
A = tuple(map(int, input().split()))
#S = [list(map(int, input().split())) for i in range(N)]
mod=998244353

ans=0
dp=[0]*(S+1)
for a in A:
    dp[0]+=1
    for i in range(S,a-1,-1):
        dp[i]+=dp[i-a]
        dp[i]%=mod
    ans+=dp[-1]
    ans%=mod
    #print(dp)

print(ans)

