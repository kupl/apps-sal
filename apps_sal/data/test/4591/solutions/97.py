(A, B, C, X, Y) = list(map(int, input().split()))
if A + B <= 2 * C:
    print(A * X + B * Y)
elif X <= Y:
    print(min(2 * C * Y, 2 * C * X + B * (Y - X)))
else:
    print(min(2 * C * X, 2 * C * Y + A * (X - Y)))
