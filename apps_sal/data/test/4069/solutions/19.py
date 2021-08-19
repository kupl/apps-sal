(X, K, D) = list(map(int, input().split()))
if X < 0:
    X = -X
if K * D < X:
    print(X - K * D)
else:
    k = K - int(X / D)
    x = X % D
    if k % 2:
        print(abs(x - D))
    else:
        print(x)
