from math import gcd
a, b, x, y = list(map(int, input().split()))
g = gcd(x, y)
x //= g
y //= g
print(min(a // x, b // y))
