(a, b) = map(int, input().split())
print(max(a + b, max(2 * a - 1, 2 * b - 1)))
