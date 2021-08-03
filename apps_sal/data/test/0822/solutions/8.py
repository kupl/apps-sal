from fractions import gcd

a, b, c = list(map(int, input().split(' ')))

a = a * b // gcd(a, b)

print(c // a)
