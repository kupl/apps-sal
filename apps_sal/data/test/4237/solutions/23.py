import math


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


A, B, C, D = map(int, input().split())
c_multiples = B // C - (A - 1) // C
d_multiples = B // D - (A - 1) // D
lcm_multiples = B // lcm(C, D) - (A - 1) // lcm(C, D)
print(B - A + 1 - c_multiples - d_multiples + lcm_multiples)
