import math
(n, r) = list(map(int, input().split()))
angle = math.pi / n
print('%.7f' % (r / (1.0 / math.sin(angle) - 1)))
