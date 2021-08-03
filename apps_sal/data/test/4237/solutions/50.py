import math as m
A, B, C, D = map(int, input().split())
A -= 1
g = C * D // m.gcd(C, D)
x = B // C - A // C
y = B // D - A // D
z = B // g - A // g
print(B - A - x - y + z)
