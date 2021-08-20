(a, b, c, x, y) = list(map(int, input().split()))
mincost = a * x + b * y
for z in range(max(x, y) + 1):
    x_ = max(0, x - z)
    y_ = max(0, y - z)
    cost = 2 * c * z + a * x_ + b * y_
    mincost = min(mincost, cost)
print(mincost)
