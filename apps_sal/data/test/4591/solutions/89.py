(A, B, C, X, Y) = list(map(int, input().split()))
ans = float('INF')
for i in range(0, 2 * max(X, Y) + 1, 2):
    ans = min(ans, int(A * max(0, X - i / 2) + B * max(0, Y - i / 2) + C * i))
print(ans)
