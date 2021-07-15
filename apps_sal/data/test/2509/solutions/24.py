n,k=list(map(int,input().split()))
ans=n*n
if k!=0:
    ans-=k*n
    for b in range(k+1,n+1):
        tmp=(n//b)*(k)+min(n%b,k-1)
        ans-=tmp
print(ans)

