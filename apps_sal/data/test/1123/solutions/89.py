N,K=map(int,input().split())
m=10**9+7
d=[0]*K
for k in range(K,0,-1):
    d[k-1]=pow(K//k,N,m)
    for l in range(2*k,K+1,k):
        d[k-1]=(d[k-1]-d[l-1])%m
print(sum([(k+1)*d[k]%m for k in range(K)])%m)
