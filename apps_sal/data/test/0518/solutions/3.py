import math
(n, r) = list(map(int, input().split()))
angle = math.pi / n
s = math.sin(angle)
print('%.8f' % (r * s / (1 - s)))
