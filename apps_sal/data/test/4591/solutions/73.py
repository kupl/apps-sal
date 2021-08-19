(A, B, C, X, Y) = list(map(int, input().split()))
ans = 10000000000
cost = 0
cost = max(X, Y) * C * 2
ans = min(ans, cost)
if X > Y:
    cost = Y * C * 2
    cost1 = cost + (X - Y) * A
    cost2 = cost + (X - Y) * C * 2
    cost = min(cost1, cost2)
    ans = min(ans, cost)
else:
    cost = X * C * 2
    cost1 = cost + (Y - X) * B
    cost2 = cost + (Y - X) * C * 2
    cost = min(cost1, cost2)
    ans = min(ans, cost)
cost = A * X + B * Y
ans = min(ans, cost)
print(ans)
