def gcd(a, b):
    while b != 0:
        a %= b
        (a, b) = (b, a)
    return a


(a, b, x, y) = [int(i) for i in input().split()]
g = gcd(x, y)
x //= g
y //= g
print(min(a // x, b // y))
