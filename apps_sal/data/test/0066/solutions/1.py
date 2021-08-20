from fractions import gcd
(a, b, c) = list(map(int, input().split(' ')))
l = b * c // gcd(b, c)
(b, c) = (min(b, c), max(b, c))
mults = a // l
rem = a - l * mults + 1
num = mults * b
rem = min(b, rem)
x = num + rem - 1
g = gcd(x, a)
print(str(x // g) + '/' + str(a // g))
