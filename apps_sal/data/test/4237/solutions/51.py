import math


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


A, B, C, D = list(map(int, input().split()))

l = lcm(C, D)

temp = l - (l // C + l // D - 1)

a = (A - 1) % l
b = B % l

aa = (A - 1) // l
bb = B // l

tempA = a - (a // C + a // D - 1)
tempB = b - (b // C + b // D - 1)


ans = temp * bb + tempB - (temp * aa + tempA)


print(ans)
