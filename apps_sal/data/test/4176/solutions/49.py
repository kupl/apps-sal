import math
A, B = map(int, input().split())


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


print(lcm(A, B))
