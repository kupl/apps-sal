(n, m) = map(int, input().split())
n = min(n, 2 * m)
m = min(m, 2 * n)
print((n + m) // 3)
