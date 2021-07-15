from operator import itemgetter, attrgetter
n,r=list(map(int,input().split()))
ps,neg=[],[]
for i in range(n):
    a,b=list(map(int,input().split()))
    if(b>=0):
        ps.append([a,b,-a-b])
    else:
        neg.append([a,b,-a-b])
ps=sorted(ps)
neg=sorted(neg,key=itemgetter(2))
ps=ps+neg
#print(*ps)
dp=[-float('inf')]*(n+1)
dp[0]=r
for i in range(n):
    for j in range(n-1,-1,-1):
        if(dp[j]>=ps[i][0]):
            dp[j+1]=max(dp[j+1],dp[j]+ps[i][1])
for j in range(n,-1,-1):
    if(dp[j]>=0):
        print(j)
        break

