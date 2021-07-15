# 改行でバグる時
import sys
input = lambda: sys.stdin.readline().rstrip()

import itertools
import bisect

n,m= list(map(int, input().split()))
w= list(map(int, input().split()))
g= [list(map(int, input().split())) for i in range(m)]
g.sort(key=lambda x:x[1])
L=[0]
V=[]
x=0
for i in range(m):
    if g[i][0]>x:
        L.append(g[i][0])
        V.append(g[i][1])
        x=g[i][0]



# どう頑張っても壊れる時を除外
w.sort()
if w[-1]>g[0][1]:
    print((-1))
    return


ANS=float('inf')
# 順序を全探索
for v in itertools.permutations(w):
    dp = [0] * n
    dp[0]=0
    for i in range(1,n):
        cnt=v[i]
        for j in range(i-1,-1,-1):
            cnt+=v[j]
            vv=bisect.bisect_left(V,cnt)
            dp[i]=max(dp[i],dp[j]+L[vv])
    ANS=min(ANS,dp[-1])
print(ANS)

