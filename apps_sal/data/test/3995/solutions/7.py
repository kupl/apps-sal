(n, k) = map(int, input().split())
print((((n - k) // 2 * '0' + '1') * (n // ((n - k) // 2 + 1) + 1))[:n])
