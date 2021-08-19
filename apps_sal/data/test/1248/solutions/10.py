(a, b, c) = map(int, input().split())
print(min(a + c + b, 2 * a + 2 * b, 2 * (a + c), 2 * (b + c)))
