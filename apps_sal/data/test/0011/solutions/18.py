from fractions import gcd
(n, a, b, p, q) = list(map(int, input().split()))
num1 = n // a
num2 = n // b
t = a * b // gcd(a, b)
num3 = n // t
print((num1 - num3) * p + (num2 - num3) * q + num3 * max(p, q))
