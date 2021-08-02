import math

gcd = 0
n = int(input())
a, b = [0] * n, [0] * n
for i in range(n):
    a[i], b[i] = list(map(int, input().split()))
    gcd = math.gcd(gcd, a[i] * b[i])
for i in range(n):
    if (math.gcd(gcd, a[i]) > 1):
        gcd = math.gcd(gcd, a[i])
    else:
        gcd = math.gcd(gcd, b[i])
print(-1 if gcd == 1 else gcd)
