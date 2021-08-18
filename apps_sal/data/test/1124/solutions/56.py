

import math

N = int(input())
a = list(map(int, input().split()))

gcd_a = a[0]
for i in range(1, N):
    gcd_a = math.gcd(gcd_a, a[i])

print(gcd_a)
