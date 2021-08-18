import math

N = int(input())
V = []
for _ in range(N):
    V.append([int(n) for n in input().split()])

R2 = 0
for i in range(100):
    theta = 2 * math.pi * i / 100
    a, b = math.cos(theta), math.sin(theta)
    X, Y = 0, 0
    for x, y in V:
        if a * x + b * y > 0:
            X += x
            Y += y
    r2 = X**2 + Y**2
    if r2 > R2:
        R2 = r2

print(math.sqrt(R2))
