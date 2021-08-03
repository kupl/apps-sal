# C - Half and Half
A, B, C, X, Y = map(int, input().split())

# AB ピザを買わない場合
pay1 = X * A + Y * B
# A ピザ を AB ピザで作る場合
pay2 = 10**10
if Y >= X:
    pay2 = C * 2 * X + B * (Y - X)
# B ピザを AB ピザで作る場合
pay3 = 10**10
if X >= Y:
    pay3 = A * (X - Y) + C * 2 * Y
# AB ピザで全部作る場合
pay4 = C * max(X, Y) * 2
print(min(pay1, pay2, pay3, pay4))
