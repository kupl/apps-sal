def gcd(x, y):
    counter = 0
    while y != 0:
        counter += x // y
        x, y = y, x % y
    return counter

x, y = map(int, input().split())
print(gcd(x, y))
