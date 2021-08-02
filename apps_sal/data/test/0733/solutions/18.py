from fractions import gcd
x, y, a, b = list(map(int, input().split()))
m = x // __import__("fractions").gcd(x, y) * y
f = (a // m) * m
if f < a:
    f += m
t = (b // m) * m
print(0 if t < f else 1 + (t - f) // m)
