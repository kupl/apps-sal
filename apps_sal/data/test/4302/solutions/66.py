(a, b) = map(int, input().split())
print(max(a + b, a + (a - 1), b + (b - 1)))
