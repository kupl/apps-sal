(a, b) = map(int, input().split())
print([a + b, 2 * max(a, b) - 1][max(a, b) - 1 >= min(a, b)])
