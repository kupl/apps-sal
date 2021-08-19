(A, B, C, X, Y) = map(int, input().split())
ans = A * X + B * Y
a = 0
b = 0
for i in range(1, 1 + 2 * max(X, Y)):
    if X - i / 2 < 0:
        a = 0
    else:
        a = X - i / 2
    if Y - i / 2 < 0:
        b = 0
    else:
        b = Y - i / 2
    ans = min(ans, A * a + B * b + C * i)
print(int(ans))
