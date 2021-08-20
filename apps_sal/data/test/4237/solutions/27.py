import math


def lcm(x, y):
    return x * y // math.gcd(x, y)


(A, B, C, D) = map(int, input().split())
x = B // lcm(C, D) - (A - 1) // lcm(C, D)
y = B // C - (A - 1) // C
z = B // D - (A - 1) // D
ans = B - A + 1 - (y + z - x)
print(ans)
