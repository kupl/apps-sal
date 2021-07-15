X, K, D = map(int, input().split())
par = K%2
if X < -K*D:
    print(-X-K*D)
elif X > K*D:
    print(X-K*D)
else:
    if par ==0:
        if X%(2*D) < D:
            print(X%(2*D))
        else:
            print(2*D-X%(2*D))
    else:
        if (X-D)%(2*D) < D:
            print((X-D)%(2*D))
        else:
            print(2*D-(X-D)%(2*D))
