# MAX-=min

# 0 <= x <= y で，gcd(x, y) = gcd(x, y - x) が成立
# gcd(a) を求めればよい

import math

N = int(input())
a = list(map(int, input().split()))

gcd_a = a[0]
for i in range(1, N):
    gcd_a = math.gcd(gcd_a, a[i])

print(gcd_a)
