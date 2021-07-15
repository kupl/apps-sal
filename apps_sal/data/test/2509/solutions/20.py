n,k=map(int,input().split())
ans=0

if k==0:
    print(n**2)
else:
    for i in range(k+1,n+1):
        if n%i<k:
            ans+=n//i*(i-k)
        else:
            ans+=n//i*(i-k)+n%i-(k-1)
    
    print(ans)
