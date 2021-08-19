import math
a, b, x = map(int, input().split())

x /= a


if x / a / b > 1 / 2:
    # ab-0.5a**2*tan(th)=x
    # tan(th)=(a*b-x)*2/a**2
    tan_th = (a * b - x) * 2 / a**2
else:
    # 0.5*b**2/tan(th)=x
    # tan(th)=b**2/2/x
    tan_th = (b**2 / 2 / x)
print(math.degrees(math.atan(tan_th)))
