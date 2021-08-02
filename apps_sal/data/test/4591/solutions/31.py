A, B, C, X, Y = map(int, input().split())

ans = 10 ** 9

for c in range(max(X, Y) + 1):
    a = max(X - c, 0)
    b = max(Y - c, 0)

    cost = A * a + B * b + C * 2 * c
    ans = min(cost, ans)

print(ans)
