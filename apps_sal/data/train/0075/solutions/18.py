from math import radians, sin, cos
t = int(input())
for _ in range(t):
    n = int(input())
    alpha = radians(90 / n)
    r = 0.5 / sin(alpha)
    beta = 180 * (n // 2) / n
    gamma = radians((90 - beta) / 2)
    d = r * cos(gamma)
    print(2 * d)
