N,K=map(int,input().split())
LR=[list(map(int,input().split())) for i in range(K)]
d=[0]*(N+1)
da=[0]*(N+1)
d[1]=da[1]=1
m=998244353
for i in range(1,N):
    for l,r in LR:
        if l<=i+1:
            d[i+1]+=da[i+1-l]-da[max(0,i-r)]
    da[i+1]=(da[i]+d[i+1])%m
print(d[-1]%m)
