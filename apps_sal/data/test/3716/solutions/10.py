n = int(input())
print(n if n < 3 else (n - 1) * (n * (n - 2) if n & 1 else (n - 3) * (n if n % 3 else n - 2)))
