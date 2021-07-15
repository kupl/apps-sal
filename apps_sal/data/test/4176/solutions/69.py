import math

a, b = map(int, input().split())

def lcm(x, y):
    return (x * y) // math.gcd(x, y)

print(lcm(a, b))
