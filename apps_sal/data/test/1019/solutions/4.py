from fractions import gcd

n = int(input())

a, b = n // 2, (n + 1) // 2

while gcd(a, b) != 1:
    a -= 1
    b += 1

print(a, b, sep=' ')
