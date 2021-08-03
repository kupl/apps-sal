a, b, c = int(input()), int(input()), int(input())
print(max((b + min(a, c)) * max(a, c), a + b + c, a * b * c))
