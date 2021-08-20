(m, b) = list(map(int, input().split()))
x = b * m
y = b
ans = 0
for i in range(y):
    xx = (b - i) * m
    ans = max(ans, xx * (xx + 1) // 2 * (i + 1) + i * (i + 1) // 2 * (xx + 1))
print(ans)
