(A, B, C, X, Y) = map(int, input().split())
if A + B < 2 * C:
    ans = A * X + B * Y
elif X <= Y:
    ans = C * 2 * X
    if 2 * C <= B:
        ans += 2 * C * (Y - X)
    else:
        ans += B * (Y - X)
else:
    ans = C * 2 * Y
    if 2 * C <= A:
        ans += 2 * C * (X - Y)
    else:
        ans += A * (X - Y)
print(ans)
