from fractions import gcd
a, b, c = map(int, input().split())
print(c // (a * b // gcd(a, b)))
