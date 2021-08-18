import math
A, B, C, D = map(int, input().split())


lcm = C * D // math.gcd(C, D)
a = B - A + 1
b = B // C - (A - 1) // C
c = B // D - (A - 1) // D
d = B // lcm - (A - 1) // lcm

print(a - b - c + d)
