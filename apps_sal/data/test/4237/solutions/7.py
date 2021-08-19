from math import gcd
(A, B, C, D) = map(int, input().split())
lcm = C * D // gcd(C, D)
a = (A - 1) // C + (A - 1) // D - (A - 1) // lcm
b = B // C + B // D - B // lcm
print(B - A + 1 - b + a)
