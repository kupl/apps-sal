def gcd(a, b):
    while (b != 0):
        x = a % b
        a = b
        b = x
    return a


a, b, x, y = list(map(int, input().strip().split(' ')))

d = gcd(x, y)
x1 = x // d
x2 = y // d

print(min(a // x1, b // x2))
