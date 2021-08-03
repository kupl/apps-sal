import math

k = int(input())
total = 0
for i in range(1, k + 1):
    for j in range(1, k + 1):
        tmp = math.gcd(i, j)
        for k in range(1, k + 1):
            total += math.gcd(tmp, k)
print(total)
