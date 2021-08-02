from math import gcd
k = int(input())
sum = 0

for a in range(1, k + 1):
    for b in range(1, k + 1):
        x = gcd(a, b)
        for c in range(1, k + 1):
            sum += gcd(x, c)

print(sum)
