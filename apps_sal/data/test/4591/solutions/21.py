A, B, C, X, Y = map(int, input().split())
ans = 2 * (5000 * 10**5)
for Z in range(10**5 + 1):
    total = A * max(X - Z, 0) + B * max(Y - Z, 0) + 2 * C * Z
    ans = min(total, ans)
print(ans)
