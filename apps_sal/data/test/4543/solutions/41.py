from math import sqrt
a, b = input().split()
n = int(a+b)
print(('Yes' if sqrt(n) == int(sqrt(n)) else 'No'))

