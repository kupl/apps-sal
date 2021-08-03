A, B, X = map(int, input().split())

if A + B > X:
    print(0)

else:
    f = 0
    while f <= 9:
        S = A * (10**f) + B * (f + 1)
        if S > X:
            break

        f += 1

    if f == 10:
        print(10**9)

    else:
        X = X - B * f
        print(min(X // A, 10**f - 1))
