n, m = map(int, input().split())
print(*[n // m + 1 if i < n % m else n // m for i in range(m)])
