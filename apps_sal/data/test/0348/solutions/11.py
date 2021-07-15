n,m,L,R=map(int,input().split())
k=R-L+1
if (n*m)%2:
    print(pow(k,n*m,998244353))
else:
    r=pow(k,n*m,998244353)
    if k%2:
        if r%2:print(((r+1)//2)%998244353)
        else:print(((r+1+998244353)//2)%998244353)
    else:
        if r%2==0:print(r//2)
        else:print((r+998244353)//2)
