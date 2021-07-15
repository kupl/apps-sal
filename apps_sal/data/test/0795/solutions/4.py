def gcd(a, b):
    c = a % b
    return gcd(b, c) if c else b
from math import sqrt
n = int(input())     
print(sum(n // (x * x + y * y) for x in range(1, int(sqrt(n // 2)) + 1) for y in range(x + 1, int(sqrt(n - x * x)) + 1, 2) if gcd(x, y) == 1))
