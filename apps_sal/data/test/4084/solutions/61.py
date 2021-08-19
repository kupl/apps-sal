(n, a, b) = map(int, input().split())
print(n // (a + b) * a + a if n - n // (a + b) * (a + b) >= a else n - n // (a + b) * b)
