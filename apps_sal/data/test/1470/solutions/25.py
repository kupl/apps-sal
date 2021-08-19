import math
x = int(input())
xi = math.floor(x / 5.5)
for i in range(xi, 10000000000000000000000000000):
    if x <= 6 * i - math.floor(i / 2):
        xa = i
        break
print(xa)
