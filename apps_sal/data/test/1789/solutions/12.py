(a, b, x, y) = map(int, input().split())
y = min(y, 2 * x)
d = abs(2 * b + 1 - 2 * a)
ans = y * (d // 2) + x
print(ans)
