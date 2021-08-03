import math
a, b, x = map(int, input().split())
if a * a * b / 2 >= x:
    print(180 * math.atan((a * b * b) / (2 * x)) / math.pi)
else:
    h = x / (a * a)
    deruta_h = b - h
    print(180 * math.atan((2 * deruta_h) / a) / math.pi)
