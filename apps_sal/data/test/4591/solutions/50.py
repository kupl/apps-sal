(A, B, C, X, Y) = list(map(int, input().split()))
ans = 10000 * 10 ** 5
for z in range(10 ** 5 + 1):
    x = max(X - z, 0)
    y = max(Y - z, 0)
    yen = A * x + B * y + 2 * C * z
    if ans > yen:
        ans = yen
print(ans)
