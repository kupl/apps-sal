def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


a, b, x, y = map(int, input().split())

g = gcd(x, y)
x //= g
y //= g

print(min(a // x, b // y))
