import math
import decimal
a, b, x = map(int, input().split(" "))
if a * a * b * 0.5 < x:  # 多い
    print(math.atan((2 * b - (2 * x / a / a)) / a) * 180 / math.pi)
else:  # 少ない
    print(90 - math.atan(2 * x / (a * b * b)) * 180 / math.pi)
