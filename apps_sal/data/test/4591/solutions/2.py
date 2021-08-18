
A, B, C, X, Y = map(int, input().split())


if 2 * C > A + B:
    print(A * X + B * Y)
else:
    if X > Y:
        print(min(2 * C * X, 2 * C * Y + A * (X - Y)))
    else:
        print(min(2 * C * Y, 2 * C * X + B * (Y - X)))
