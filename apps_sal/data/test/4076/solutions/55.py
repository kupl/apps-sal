import math
a, b, h, m = [int(x) for x in input().split()]
p = math.pi
arg_h = 2 * p * h / 12 + m * p / 360
arg_m = 2 * p * m / 60
arg = abs(arg_h - arg_m)
c_2 = a**2 + b**2 - 2 * a * b * math.cos(arg)
c = math.sqrt(c_2)
print(c)
