import math
N = int(input())
gcd = 1
for i in range(2, N + 1):
    gcd = gcd * i // math.gcd(gcd, i)
print(gcd + 1)
