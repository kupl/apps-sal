from math import *

n, r = map(int, input().split())
u = tan(2 * pi / n) * cos(pi / n) - sin(pi / n)
u = u * u
v = tan(2 * pi / n)
v = v * v + 1

a = u - v
b = 2 * r * u
c = r * r * u

R = (- b + sqrt(b * b - 4 * a * c)) / (2 * a)
if R <= 0:
    R = (- b - sqrt(b * b - 4 * a * c)) / (2 * a)

print(R)
