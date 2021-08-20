(a, b, c, x, y) = map(int, input().split())
ans = 0
ab = min(a + b, c * 2)
temp = min(x, y)
ans += ab * temp
x -= temp
y -= temp
ans += min(a, c * 2) * x
ans += min(b, c * 2) * y
print(ans)
