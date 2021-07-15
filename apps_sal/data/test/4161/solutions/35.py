import math
from functools import reduce

k = int(input())

ans = 0

gcd_sum = [0] * 201

for i in range(1, k + 1):
    for j in range(1, k + 1):
        gcd_sum[i] += math.gcd(i, j)

for a in range(1, k + 1):
    for b in range(1, k + 1):
        _gcd = math.gcd(a,b)
        ans += gcd_sum[_gcd]

print(ans)

