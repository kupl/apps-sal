a, b, x, y = list(map(int, input().split()))
from math import gcd
g = gcd(x, y)
x //= g
y //= g
print(min(a // x, b // y))

