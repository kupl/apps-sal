import math

A, B, C, D = map(int, input().split())

c = B // C - (A - 1) // C
d = B // D - (A - 1) // D
lcm = C * D // math.gcd(C, D)
cd = B // lcm - (A - 1) // lcm

x = c + d - cd
print(B - A + 1 - x)
