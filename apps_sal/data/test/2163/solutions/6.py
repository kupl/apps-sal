(n, m) = map(int, input().split())
(x, y, M) = (0, 1, 1000000007)
for i in range(n):
    x = ((2 * m - 1) * x + y) % M
    y = y * m % M
print((y + m * x) % M)
