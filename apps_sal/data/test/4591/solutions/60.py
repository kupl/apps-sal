(A, B, C, X, Y) = map(int, input().split())
res = 2 * C * max(X, Y)
if X > Y:
    res = min(2 * C * Y + (X - Y) * A, res)
else:
    res = min(2 * C * X + (Y - X) * B, res)
res = min(A * X + B * Y, res)
print(res)
