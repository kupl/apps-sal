A, B, C, X, Y = map(int, input().split())

pay1 = X * A + Y * B
pay2 = 10**10
if Y >= X:
    pay2 = C * 2 * X + B * (Y - X)
pay3 = 10**10
if X >= Y:
    pay3 = A * (X - Y) + C * 2 * Y
pay4 = C * max(X, Y) * 2
print(min(pay1, pay2, pay3, pay4))
