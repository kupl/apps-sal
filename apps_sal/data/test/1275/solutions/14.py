(n, k) = map(int, input().split())
k = abs(k)
ans = 0
for i in range(k + 2, 2 * n + 1):
    x = min(i - 1, 2 * n - i + 1)
    y = min(i - 1 - k, 2 * n + 1 - (i - k))
    ans += x * y
print(ans)
