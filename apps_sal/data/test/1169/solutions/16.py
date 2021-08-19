(n, m) = list(map(int, input().split()))
i = 0
while i * (i - 1) / 2 < m and i <= n:
    i += 1
if n // 2 + n % 2 <= m:
    print(0, n - i)
else:
    print(n - 2 * m, n - i)
