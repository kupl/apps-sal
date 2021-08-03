from math import gcd
K = int(input())
k = [1, 1, 1]
g = 0
for a in range(1, K + 1):
    for b in range(1, K + 1):
        for c in range(1, K + 1):
            g += gcd(gcd(a, b), c)


print(g)
