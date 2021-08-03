n, x, t = map(int, input().split())
print(n // x * t if n % x == 0 else (n // x + 1) * t)
