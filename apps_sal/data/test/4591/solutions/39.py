a, b, c, x, y = map(int, input().split())
ans = 0
ans += 2 * c * min(x, y)
if x < y:
    ans += (y - x) * b
else:
    ans += (x - y) * a

ans = min(ans, a * x + b * y)
print(min(ans, 2 * c * max(x, y)))
