import math

n, r = list(map(int, input().split()))
angle = math.pi / n
s = math.sin(angle)
#rad = 1 / math.sin(angle) - 1
#print('%.8f' % (r / rad))
print('%.8f' % (r * s / (1 - s)))

