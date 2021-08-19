(n, a, b, c, d) = list(map(int, input().split()))
ans = 0
for x1 in range(1, n + 1):
    x2 = x1 + b - c
    x4 = a + x1 - d
    x5 = b + x4 - c
    if 1 <= x2 <= n and 1 <= x4 <= n and (1 <= x5 <= n):
        ans += 1
print(ans * n)
