(n, m) = map(int, input().split())
i = b = 0
a = 1
while i < n:
    c = (m - i) * ((m - n + i) * a + (m - i + 1) * i * b) % (10 ** 9 + 7)
    i += 1
    (a, b) = (c, a)
print(a)
