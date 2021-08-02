import math
a, b, c, d = list(map(int, input().split(' ')))
if d / b <= c:
    print(min(d * int(a / b) + a % b * c, d * math.ceil(a / b)))
else:
    print(a * c)
