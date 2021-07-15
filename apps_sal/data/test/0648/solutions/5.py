m, b = map(int, input().split())
res = 0
for i in range(b + 1):
    res = max(res, (m * i * (m * i + 1) // 2) * (b - i + 1) + ((b - i) * (b - i + 1) // 2) * (m * i + 1))
print(res)
