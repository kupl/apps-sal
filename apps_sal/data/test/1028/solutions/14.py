n, m = list(map(int, input().split()))

a, c = divmod(n, m)
b = n - m + 1

print((a * (a - 1) >> 1) * (m - c) + ((a + 1) * a >> 1) * c, b * (b - 1) >> 1)
