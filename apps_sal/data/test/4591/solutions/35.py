a, b, c, x, y = list(map(int, input().split()))
ans = int(1e9)
for i in range(max(x, y) * 2 + 1):
    ans = min(ans, c * i + a * max(0, x - i // 2) + b * max(0, y - i // 2))

print(ans)
