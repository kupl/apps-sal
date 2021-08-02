import math
from functools import reduce


def gcd(*numbers):
    return reduce(math.gcd, numbers)


def gcd_list(numbers):
    return reduce(math.gcd, numbers)


k = int(input())
p = 0
ans = 0
if k > 2:
    for i in range(1, k - 1):
        for j in range(i + 1, k):
            for m in range(j + 1, k + 1):
                ans += gcd(i, j, m)
p += 6 * ans
b = 0
for i in range(1, k):
    for j in range(i + 1, k + 1):
        b += math.gcd(i, j)
p += 6 * b + k * (k + 1) // 2
print(p)
