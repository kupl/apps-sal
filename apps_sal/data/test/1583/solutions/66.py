import math
a, b, x = map(int, input().split())

S = a * b
s = x / a
if s == S:
    print(0)

elif s >= S / 2:
    em_s = S - s
    tan = (a**2) / (2 * em_s)
    ans = math.degrees(math.atan(tan))
    print(90 - ans)

else:
    tan = (2 * s) / (b**2)
    ans = math.degrees(math.atan(tan))
    print(90 - ans)
