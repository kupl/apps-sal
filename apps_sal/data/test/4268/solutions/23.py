import math
n,d=map(int,input().split())
x=[list(map(int,input().split())) for i in range (n)]
ans=0
for i in range(n-1):
    for j in range(i+1,n):
        tmp=0
        for k in range(d):
            tmp+=(x[i][k]-x[j][k])**2
        if math.sqrt(tmp)==int(math.sqrt(tmp)):
            ans+=1
print(ans)
