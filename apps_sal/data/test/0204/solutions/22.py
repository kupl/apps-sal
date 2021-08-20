from math import gcd
(a, b, x, y) = map(int, input().split(' '))
g = gcd(x, y)
n1 = a * g // x
n2 = b * g // y
print(min(n1, n2))
