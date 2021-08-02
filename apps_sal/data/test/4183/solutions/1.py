import math


def lcm(x, y):
    return x * y // math.gcd(x, y)


n = int(input())
t = int(input())

for i in range(n - 1):
    num = int(input())
    t = lcm(t, num)
print(t)
