# C - : (Colon)

import math

a, b, h, m = list(map(int, input().split()))

s = 3600 * h + 60 * m
radh = ((s / (60 * 60 * 12)) - int(s / (60 * 60 * 12))) * 2 * math.pi
radm = ((s / (60 * 60)) - int(s / (60 * 60))) * 2 * math.pi

c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(radh - radm))

print(c)
