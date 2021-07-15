n = int(input())
print(max(n, (n // 100 if n > 0 else -((-n) // 100)) * 10 + (n % 10 if n > 0 else -((-n) % 10)), n // 10 if n > 0 else -((-n) // 10)))
