import math
(a, b, h, m) = map(int, input().split())
ha = (h * 60 + m) / 360 * math.pi
ma = m / 30 * math.pi
(sh, ch) = (math.sin(ha), math.cos(ha))
(sm, cm) = (math.sin(ma), math.cos(ma))
print(((a * sh - b * sm) ** 2 + (a * ch - b * cm) ** 2) ** (1 / 2))
