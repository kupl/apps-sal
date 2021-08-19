import math
N = int(input())


def lcm(x, y):
    return x * y // math.gcd(x, y)


g = 1
for i in range(2, N + 1):
    g = lcm(g, i)
print(g + 1)
