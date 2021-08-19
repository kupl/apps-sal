import math
(l3, l4, l5) = list(map(int, input().split(' ')))
v3 = l3 ** 3 * math.sqrt(2) / 12
v4 = l4 ** 3 / math.sqrt(2) / 3
alpha = math.pi / 5
v5 = 5 / 12 * l5 ** 3 / math.tan(alpha) * math.sqrt(1 - 1 / (4 * math.sin(alpha) ** 2))
print('%.11f' % (v3 + v4 + v5))
