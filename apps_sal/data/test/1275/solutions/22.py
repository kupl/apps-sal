n, k = map(int, input().split())
k = abs(k)
ans = 0
for i in range(2 + k, 2 * n + 1):
    ans += min(2 * n - i + k + 1, i - k - 1) * min(2 * n - i + 1, i - 1)
print(ans)
