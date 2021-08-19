(n, k) = map(int, input().split())
a = 0
for b in range(1, n + 1):
    (p, q) = divmod(n, b)
    a += max(0, b - k) * p + max(0, q - k + 1)
print(a if k else n * n)
