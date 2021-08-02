import math


def DegToRad(x):
    return (math.acos(-1) / 180) * x


l3, l4, l5 = map(int, input().split())
v3 = l3 * l3 * l3 * math.sqrt(2) / 12
v4 = l4 * l4 * l4 * math.sqrt(2) / 6
a = l5; b = a / math.sqrt(2 - 2 * math.cos(DegToRad(72))); h = math.sqrt(a * a - b * b); s = b * b * math.sin(DegToRad(72)) * 2.5; v5 = s * h / 3;
print(v3 + v4 + v5)
