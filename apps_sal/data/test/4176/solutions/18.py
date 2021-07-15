from math import gcd
a, b = [int(i) for i in input().split()]
print(int(a * b / gcd(a, b)))
