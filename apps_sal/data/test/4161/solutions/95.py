from math import gcd

k = int(input())
result = 0

for a in range(1, k + 1):
    for b in range(1, k + 1):
        for c in range(1, k + 1):
            result += gcd(gcd(a, b), c)

print(result)
