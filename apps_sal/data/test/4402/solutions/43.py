a, b = map(int, input().split())
print(b if a >= 13 else 0 if a <= 5 else b//2)
