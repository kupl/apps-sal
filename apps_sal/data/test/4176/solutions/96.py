import math
a, b = map(int, input().split())


def lcm(x, y):  # Least common multiple
    return (x * y) // math.gcd(x, y)


print(lcm(a, b))
