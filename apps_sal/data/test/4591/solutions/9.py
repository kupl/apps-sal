A, B, C, X, Y = list(map(int, input().split()))

ans = 0

if A + B > 2 * C:
    ans += 2 * C * min(X, Y)
    if X > Y:
        ans += (X - Y) * min(2 * C, A)
    else:
        ans += (Y - X) * min(2 * C, B)
else:
    ans = A * X + B * Y
print(ans)
