X, K, D = list(map(int, input().split()))

if abs(X) >= K * D:
    print((abs(X) - K * D))
else:
    n = abs(X) // D
    p = abs(X) % D
    if (K-n) % 2 == 0:
        print(p)
    else:
        print((D-p))


