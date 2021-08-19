import math
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
if n == 1:
    print(a[0])
else:
    lcm = a[0] * a[1] // math.gcd(a[0], a[1])
    for i in range(2, n):
        lcm = lcm * a[i] // math.gcd(lcm, a[i])
    print(lcm)
