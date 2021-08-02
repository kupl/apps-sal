n, m = map(int, input().split())
i, a, b = 0, 1, 0
while i < n:
    c = ((m - i) * ((m - n + i) * a + i * b * (m - i + 1))) % (10**9 + 7)
    i += 1
    a, b = c, a
print(a)
