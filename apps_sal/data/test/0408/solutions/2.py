n, m = list(map(int, input().split()))
n = min(2 * m, n)
m = min(2 * n, m)
print((n + m) // 3)
