
a, b, c = map(int, input().split())
x = min(a, b - 1, c - 2)
print(x + x + 1 + x + 2)
