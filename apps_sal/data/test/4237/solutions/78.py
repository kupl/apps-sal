from fractions import gcd
def lcm(x, y): return x * y // gcd(x, y)


A, B, C, D = map(int, input().split())

Cwareru = B // C - (A - 1) // C
Dwareru = B // D - (A - 1) // D
CDwareru = B // lcm(C, D) - (A - 1) // lcm(C, D)
# print(Cwareru,Dwareru,CDwareru)
print(B - A + 1 - (Cwareru + Dwareru - CDwareru))
