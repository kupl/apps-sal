from fractions import gcd
a, b, x, y = list(map(int, input().split()))


x, y = x // gcd(x, y), y // gcd(x, y)

print(min(a // x, b // y))
