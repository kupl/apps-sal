import math
(n, r) = list(map(int, input().split()))
angle = math.pi / n
c = math.sin(angle)
k = c / (1 - c)
R = k * r
R = float(format(R, '.7f'))
print(R)
