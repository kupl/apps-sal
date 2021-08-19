(a, b, c) = list(map(int, input().split()))
print(min(min(a + b + c, 2 * (a + b)), min(2 * (a + c), 2 * (b + c))))
