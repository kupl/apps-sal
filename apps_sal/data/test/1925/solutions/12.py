from math import floor
a, b, n = map(int, input().split())
x = min(n, b - 1)
print(floor(a * x / b) - a * floor(x / b))
