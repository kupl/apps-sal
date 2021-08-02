from math import gcd

n = int(input())
k = 0
num = n * n
for a in range(2, int((n + 1)**0.5) + 2):
    for b in range((a & 1) + 1, a, 2):
        z = (a**2 + b**2)
        if z > num:
            break
        if gcd(a, b) == 1:
            k += int(n / z)
print(k)
