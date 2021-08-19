(a, b, c) = map(int, input().split())
print(min(a, b - 1, c - 2) * 3 + 3)
