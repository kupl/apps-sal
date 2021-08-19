(a, b, c, x, y) = map(int, input().split())
ans = 10000000000.0
for k in range(100010):
    ans = min(2 * c * k + max(x - k, 0) * a + max(y - k, 0) * b, ans)
print(int(ans))
