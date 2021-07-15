X, K, D = list(map(int, input().split()))
X = abs(X)
if X - K * D >= 0:
    print((X - K * D))
    return
else:
    n = X // D
    x = X - n * D
    if (K - n) % 2 == 0:
        print(x)
    else:
        print((min(x + D, D - x)))

