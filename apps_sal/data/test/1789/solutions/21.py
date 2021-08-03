a, b, x, y = map(int, input().split())

ans = x + abs(b - a) * y
ans = min(ans, abs(b - a) * x + abs(b - a + 1) * x)

if a > b:
    ans = min(ans, x + abs(a - b - 1) * y)
    ans = min(ans, abs(a - b) * x * 2)

print(ans)
