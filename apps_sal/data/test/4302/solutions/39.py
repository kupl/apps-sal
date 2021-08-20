(a, b) = map(int, input().split())
if a == b:
    print(a + b)
else:
    print(max(2 * a - 1, 2 * b - 1))
