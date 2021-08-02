from math import *


def GCD(a, b):
    while (b):
        a %= b
        a, b = b, a
    return a


a, b, c, d = map(int, input().split())
C, D = min(a * d, b * c), max(a * d, b * c)
C = D - C
G = GCD(C, D)
C = C // G
D = D // G
print(str(C) + "/" + str(D))
