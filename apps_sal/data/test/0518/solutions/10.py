import math

n, r = map(int, input().split())
s = math.sin(math.pi / n)
print('%.7lf' % (r * s / (1 - s)))
