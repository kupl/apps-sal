from fractions import gcd, Fraction

n = int(input())
p = Fraction(0)

for i in range(n + 1):
    if n - i <= i:
        break
    if gcd(i, n - i) == 1:
        p = max(p, Fraction(i, n - i))

a, b = str(p).split('/')
print(a, b)
