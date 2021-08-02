from fractions import gcd
n = int(input())

for a in reversed(range(1, n // 2 + 1)):
    b = n - a
    if gcd(a, b) == 1:
        print(a, b)
        break
