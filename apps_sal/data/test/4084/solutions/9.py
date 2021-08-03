n, a, b = map(int, input().split())

print(0 if a == 0 else n if a > n else a if (a + b) > n else n // (a + b) * a + (n % (a + b) if n % (a + b) < a else a))
