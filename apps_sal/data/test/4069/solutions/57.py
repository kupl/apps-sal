X,K,D=list(map(int,input().split()))
if X<0:
    X=-X
if X-K*D>=0:
    print(X-K*D)
else:
    N=X//D
    if (K-N)%2==0:
        print(X-N*D)
    else:
        print((N+1)*D-X)
