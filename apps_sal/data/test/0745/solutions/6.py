n,k=map(int,input().split())
if k>=n:print(0)
else:
    m=998244353
    L=[1]
    for i in range(1,n+1):
        L.append((L[-1]*i)%m)
    def comb(n,k):
        return (L[n]*pow((L[n-k]*L[k]),m-2,m))%m
    c=0
    for i in range(n-k):
        c+=((-1)**i*pow(n-k-i,n,m)*comb(n-k,n-k-i))%m
    c*=2
    c%=m
    c*=comb(n,n-k)
    c%=m
    if k==0:print(L[n])
    else:print(c)
