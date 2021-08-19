import math
a = 1
n = int(input())
for i in range(n):
    t = int(input())
    a = a * t // math.gcd(a, t)
print(a)
