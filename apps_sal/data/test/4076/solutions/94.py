import math
a, b, h, m = list(map(int, input().split()))
ang = abs(h * 30 + m * 0.5 - m * 6)
print(math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(ang * math.pi / 180)))
