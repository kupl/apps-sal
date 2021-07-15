import math
n,m,k=list(map(int,input().split()))
if k>n+m-2 :
    print(-1)
    return
if n%(k+1)==0 :
    print(int(n/(k+1))*m)
    return
if m%(k+1)==0 :
    print(int(m/(k+1))*n)
    return
r=max(n//(k+1),1)
r1=max(0,k-n+1)
r2=m//(1+r1)
ans=r*r2
r=max(m//(k+1),1)
r1=max(0,k-m+1)
r2=n//(1+r1)
ans=max(ans,r*r2)
print(int(ans))
        
    

