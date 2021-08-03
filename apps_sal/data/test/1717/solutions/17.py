import math


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


n = int(input())
num = 1
for i in range(2, n + 1):
    num = lcm(num, i)
print(num + 1)
