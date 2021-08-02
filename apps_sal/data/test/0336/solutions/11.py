n, a, b, c, d = map(int, input().split())

ans = 0
for i in range(1, n + 1):
    s = a + b + i
    j = s - a - c
    k = s - b - d
    l = s - c - d
    if 1 <= j <= n and 1 <= k <= n and 1 <= l <= n:
        ans += n

print(ans)
