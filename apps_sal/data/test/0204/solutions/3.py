from fractions import gcd as g
(a, b, x, y) = list(map(int, input().split()))
k = g(x, y)
x //= k
y //= k
print(min(a // x, b // y))
