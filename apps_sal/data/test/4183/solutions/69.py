import math
n = int(input())
a = int(input())

if n == 1:
    print(a)
    return

b = int(input())
c = (a * b) // math.gcd(a, b)
for i in range(n - 2):
    b = int(input())
    c = (c * b) // math.gcd(c, b)

print(c)
