import math
Pi = math.pi
n, r = list(map(float, input().split()))
x = math.tan (Pi / n)
y = math.tan (Pi / n / 2)
base = r / (1 / x + 1 / y)
print(n * r * base)

