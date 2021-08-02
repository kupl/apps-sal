A, B, C, X, Y = map(int, input().split())
ans = float("inf")
for i in range(0, max(X, Y) * 2 + 1, 2):
    x = max(0, X - i // 2)
    y = max(0, Y - i // 2)
    ans = min(ans, A * x + B * y + C * i)
print(ans)
