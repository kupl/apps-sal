import math

a, b, n = map(int, input().split())

if n < b:
    c = math.floor(a * n / b)
    print(c)
else:
    c = math.floor(a * (b - 1) / b)
    print(c)
