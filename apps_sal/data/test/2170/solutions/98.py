(n, m) = map(int, input().split())
i = b = 0
a = 1
while i < n:
    (a, b) = ((m - i) * ((m - n + i) * a + i * (m - i + 1) * b) % (10 ** 9 + 7), a)
    i += 1
print(a)
