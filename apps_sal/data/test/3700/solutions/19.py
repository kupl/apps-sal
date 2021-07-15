n, m = map(int, input().strip().split())
if m <= n:
    print((m - 1) // 2)
elif 2 * n <= m:
    print(0)
else:
    print((2 * n - m + 1) // 2)
