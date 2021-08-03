import math
a, b, x = [int(r) for r in input().split(' ') if len(r) > 0]

if 2 * x >= a * a * b:
    # 半分より多い
    print(90 - math.degrees((math.atan2(a, 2 * (b - x / a**2)))))
else:
    # 半分より少ない
    print(90 - math.degrees(math.atan2((2 * x) / (a * b), b)))
