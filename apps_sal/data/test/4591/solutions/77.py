A, B, C, X, Y = list(map(int, input().split()))

ans = float("inf")
for c in range(200_001):
    cost = c * C
    cost += A * max(0, X - c // 2)
    cost += B * max(0, Y - c // 2)
    ans = min(ans, cost)
print(ans)

