import math
A, B, C, D = map(int, input().split())

# CでもDでも割り切れない = 全体(a) - Cで割り切れる(b) + Dで割り切れる(c) + CでもDでも割り切れる(d)
lcm = C * D // math.gcd(C, D)
a = B - A + 1
b = B // C - (A - 1) // C
c = B // D - (A - 1) // D
d = B // lcm - (A - 1) // lcm

print(a - b - c + d)
