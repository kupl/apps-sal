(a, b, c) = map(int, input().split())
print(min(2 * a + 2 * b, 2 * a + 2 * c, 2 * b + 2 * c, a + b + c))
