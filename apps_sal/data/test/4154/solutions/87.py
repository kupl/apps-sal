n,m=list(map(int,input().split()))
lmax,rmin=1,n
for _ in range(m):
    l,r=list(map(int,input().split()))
    lmax=max(lmax,l)
    rmin=min(rmin,r)
print((max(0,rmin-lmax+1)))

