N,s,t=list(map(int,input().split()))

A=list(map(int,input().split()))

s-=1
t-=1
ans=0
Taken=[False]*(N+1)
while(Taken[s]==False and s!=t):
    Taken[s]=True
    s=A[s]-1
    ans+=1

if(s==t):
    print(ans)
else:
    print(-1)
    

