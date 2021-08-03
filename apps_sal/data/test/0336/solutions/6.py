n, a, b, c, d = list(map(int, input().split()))
ans = 0
for i in range(1, n + 1):
    s = i + a + b
    x2 = s - a - c
    x3 = s - c - d
    x4 = s - b - d
    if max(x2, x3, x4) <= n and min(x2, x3, x4) >= 1:
        ans += n
print(ans)
