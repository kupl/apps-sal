[X, K, D] = [int(i) for i in input().split()]
X = abs(X)
if X - K * D > 0:
    print(X - K * D)
else:
    time = int(X / D)
    start = X - D * time
    time_re = K - time
    if time_re % 2 == 0:
        print(start)
    else:
        print(abs(start - D))
