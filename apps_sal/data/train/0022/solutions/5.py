t=int(input())
for _ in range(t):
    N,K=map(int,input().split())
    while(K>1):
        x=list(str(N))
        if('0' in x):
            break
        x=[int(i) for i in x]
        N=N+min(x)*max(x)
        K-=1
    print(N)
