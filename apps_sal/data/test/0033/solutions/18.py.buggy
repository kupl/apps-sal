import sys
# Uz ma to pretekanie nebavi!!!


def gcd(a, b):
    if b == 0:
        return [a, 1, 0]
    c = a % b
    [g, x1, y1] = gcd(b, c)
    x = y1
    y = x1 - y1 * (a // b)
    return [g, x, y]


a1, b1, a2, b2, l, r = [int(i) for i in input().split(" ")]
if max(b1, b2) > r:
    print(0)
    return

l = max(l, b1, b2)
[g, xg, yg] = gcd(a1, a2)
if (b2 - b1) % g == 0:
    xg *= (b2 - b1) // g
else:
    print(0)
    return
lcm = (a1 * a2) // g
val = xg * a1 + b1
if val >= l:
    val -= (((val - l) // lcm) + 1) * lcm

print(((r - val) // lcm) - ((l - val - 1) // lcm))
