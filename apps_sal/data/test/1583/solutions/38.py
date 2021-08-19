import math
(a, b, x) = map(int, input().split())
L = b * a ** 2
if L == x:
    alfa = 0
elif x >= L / 2:
    h = x / a ** 2
    beta = math.atan(a / 2 / (b - h))
    alfa = math.pi / 2 - beta
else:
    alfa = math.atan(b / (2 * x / (a * b)))
print(math.degrees(alfa))
