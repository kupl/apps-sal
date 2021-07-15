import math
n=int(input())
l=list(map(int,input().split()))
ans=0
for i in range(2,n-2):
    if(l[i]==1 and l[i-1]==0 and l[i-2]==1 and l[i+1]==0 and l[i+2]==1):
        l[i]=0
        ans+=1
for i in range(1,n-1):
    if(l[i]==0 and l[i-1]==1 and l[i+1]==1):
        ans+=1
print(ans)
