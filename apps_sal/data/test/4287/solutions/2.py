#     Codeforces Round #486 (Div. 3)

from functools import cmp_to_key
#key=cmp_to_key(lambda x,y: 1 if x not in y else -1 )

import sys
def getIntList():
    return list(map(int, input().split()))    



a,n,m = getIntList()
rainend = set()
umbr = {}
keyPointSet = set([0,a])
for i in range(n):
    t =tuple(getIntList()) 
    for j in range(t[0] + 1, t[1] + 1):
        rainend.add(j)
    keyPointSet.add(t[1])
for i in range(m):
    t =getIntList()
    if t[0] not in umbr or t[1]< umbr[t[0]]:
        umbr[t[0]] = t[1]
    keyPointSet.add(t[0])
    
keyPoint = list(keyPointSet)
keyPoint.sort()



dp = {}

dp[0] =  {}
dp[0] [0] = 0
if 0 in umbr:
    dp[0][umbr[0]] = 0


for i in range(1, len(keyPoint)):
    x = keyPoint[i]
    lx = keyPoint[i-1]
    ifrain =  x in rainend
    dp[x] = {}
    nowdp = dp[x]
    lastdp = dp[lx]
    
    for z in lastdp:
        if z == 0 :
            if not ifrain:
                nowdp[0] = lastdp[0]
        else:
            nowdp[z]  = lastdp[z] + z * (x-lx)
    if len(nowdp) >0:
        nowdp[0] = min(nowdp.values())
        if x in umbr:
            if umbr[x] not in nowdp or   nowdp[0] < nowdp[umbr[x]]:
                nowdp[umbr[x]] = nowdp[0]
    else:
        print(-1)
        return

print( min(dp[a].values()) )
            
    

