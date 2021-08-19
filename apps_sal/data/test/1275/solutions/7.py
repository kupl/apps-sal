(n, k) = map(int, input().split())
ans = 0
for i in range(2, 2 * n + 1):
    if 2 <= i - k <= 2 * n:
        ans += min(2 * n + 1 - i, i - 1) * min(2 * n + 1 - i + k, i - k - 1)
print(ans)
