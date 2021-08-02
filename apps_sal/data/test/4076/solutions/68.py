import math
from decimal import Decimal
hour_len, minute_len, hour, minute = list(map(int, input().split()))

rad_h = math.radians(Decimal((hour * 60 + minute) / 720 * 360))
rad_m = math.radians(Decimal(minute / 60 * 360))
cos_hm = math.cos(abs(Decimal(rad_h - rad_m)))

a_double = hour_len ** 2 + minute_len ** 2 - (2 * hour_len * minute_len * cos_hm)
ans = math.sqrt(a_double)
print(f"{ans:.20f}")
