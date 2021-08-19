(a, b, c) = map(int, input().split())
x = min(a, b, c)
z = max(a, b, c)
y = a + b + c - x - z
print(x + y)
