(a, b, c, x, y) = map(int, input().split())
mast = max(x, y)
ans = float('INF')
for i in range(mast + 1):
    price = a * max(x - i, 0) + b * max(y - i, 0) + c * 2 * i
    ans = min(ans, price)
print(ans)
