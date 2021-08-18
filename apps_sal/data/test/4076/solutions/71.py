import math
from decimal import Decimal
hour_len, minute_len, hour, minute = list(map(int, input().split()))

degree_hm = abs(((hour * 60 + minute) * 0.5) - (minute * 6))
rad_hm = math.radians(degree_hm)
cos_hm = math.cos(rad_hm)

a_double = hour_len ** 2 + minute_len ** 2 - (2 * hour_len * minute_len * cos_hm)
ans = math.sqrt(a_double)
print(f"{ans:.20f}")
