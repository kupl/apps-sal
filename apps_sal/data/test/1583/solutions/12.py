import math
a, b, x = map(int, input().split())
y = (a**2) * b
h = x / (a**2)


def get_angle_from_sides(a, b, c):
    return math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))


def checkio(a, b, c):
    try:
        angles = [get_angle_from_sides(*abc) for abc in ((a, b, c), (b, c, a), (c, a, b))]
        result = sorted((math.degrees(a)) for a in angles)
        return [0, 0, 0] if 0 in result else result
    except ValueError:
        return [0, 0, 0]


count = 0
if y == x:
    pass
elif y / 2 <= x:
    if a >= 2 * (b - h):
        m = checkio(a, 2 * (b - h), math.sqrt(a**2 + (2 * (b - h))**2))
        count = m[0]
    elif a < 2 * (b - h):
        m = checkio(a, 2 * (b - h), math.sqrt(a**2 + (2 * (b - h))**2))
        count = m[1]
elif y / 2 > x:
    z = 2 * x / (a * b)
    if b >= z:
        m = checkio(b, z, math.sqrt(b**2 + (z)**2))
        count = m[1]
    elif b < z:
        m = checkio(b, z, math.sqrt(b**2 + (z)**2))
        count = m[0]
# print(a,2*(b-h),math.sqrt(a**2+2*(b-h)**2),m)
print(count)
