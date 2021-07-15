X,K,D=list(map(int,input().split()))
X=abs(X)
if K*D<X:
    print((X-K*D))
else:
    K-=X//D
    X%=D
    if K%2==0:
        print(X)
    else:
        print((D-X))

