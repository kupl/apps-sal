x, y, z = map(int, input().split())
ans = 0
ans += 2 * z + 2 * min(y, x)
f = min(y, x)
y = y - f
x = x - f
print(ans + min(1, max(y, x)))
