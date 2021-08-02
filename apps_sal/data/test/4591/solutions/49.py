A, B, C, X, Y = map(int, input().split())

ans = 0
if C * 2 <= A + B:
    mi = min(X, Y)
    ans = mi * C * 2
    if Y <= X:
        ans += min(A * (X - mi), 2 * C * (X - mi))
    else:
        ans += min(B * (Y - mi), 2 * C * (Y - mi))
else:
    ans = A * X + B * Y
print(ans)
