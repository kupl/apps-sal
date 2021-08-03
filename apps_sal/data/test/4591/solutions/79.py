a, b, c, x, y = list(map(int, input().split()))

ans = a * x + b * y
for i in range(1, max(x, y) + 1):
    C = 2 * i * c + a * max(0, x - i) + b * max(0, y - i)
    ans = min(ans, C)
print(ans)
