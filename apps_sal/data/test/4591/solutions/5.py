(A, B, C, X, Y) = list(map(int, input().split()))
result = []
if X > Y:
    result.append(A * X + B * Y + C * 0)
    result.append(A * (X - Y) + B * 0 + C * 2 * min(X, Y))
    result.append(A * 0 + B * 0 + C * 2 * max(X, Y))
elif X < Y:
    result.append(A * X + B * Y + C * 0)
    result.append(A * 0 + B * (Y - X) + C * 2 * min(X, Y))
    result.append(A * 0 + B * 0 + C * 2 * max(X, Y))
else:
    result.append(A * X + B * Y + C * 0)
    result.append(A * 0 + B * 0 + C * 2 * max(X, Y))
print(min(result))
