(a, b) = map(int, input().split())
print(b if a >= 13 else b // 2 if a >= 6 and a <= 12 else 0)
