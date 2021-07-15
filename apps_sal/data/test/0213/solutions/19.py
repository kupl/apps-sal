n,m=list(map(int,input().split()))
k=[0]*m
f=[0]*m
l=1
r=100
for i in range(m):
    k[i],f[i]=list(map(int,input().split()))
for i in range(m):
    fl=True
    for kol in range(l,r+1):
        ch=k[i]-(f[i]-1)*kol
        if ch>0 and ch<=kol:
            if fl:
                l=kol
                fl=False
        elif not fl:
            r=kol-1
            break
    if r-l==0:
        print((n+r-1)//r)
        break
else:
    kok=(n+r-1)//r
    for kol in range(l,r):
        if kok!=(n+kol-1)//kol:
            print(-1)
            break
    else:
        print(kok)
                

