def gcd(x, y):
    if x < y:
        (x, y) = (y, x)
    while x % y != 0:
        (x, y) = (y, x % y)
    return y


def lcm(x, y):
    return x * y // gcd(x, y)


(x, y, a, b) = (int(i) for i in input().split(' '))
f = lcm(x, y)
k = b // f - (a - 1) // f
print(k)
