import math


def LI():
    return list(map(int, input().split()))


a, b, x = LI()
if x == (a**2 * b) / 2:
    ans = 45
elif x > (a**2 * b) / 2:
    ans = math.degrees(math.atan((2 * (b - x / (a**2))) / a))
else:
    ans = math.degrees(math.atan(a * b**2 / (2 * x)))
print(ans)
