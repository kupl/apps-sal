import math


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


A, B, C, D = map(int, input().split())
CD_lcm = lcm(C, D)

B_s = B - B // C - B // D + B // CD_lcm
A_s = (A - 1) - (A - 1) // C - (A - 1) // D + (A - 1) // CD_lcm
print(B_s - A_s)
