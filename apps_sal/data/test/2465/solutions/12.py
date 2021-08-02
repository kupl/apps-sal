import math

T = int(input())
for _ in range(T):
    ang = int(input())
    t = math.gcd(ang, 180)
    possiblek = ang // t
    possiblen = 180 // t
    if possiblek <= possiblen - 2:
        print(possiblen)
    else:
        print(possiblen * 2)
