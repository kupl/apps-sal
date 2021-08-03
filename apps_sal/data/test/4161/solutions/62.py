import math
n = int(input())
c = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        d = math.gcd(i, j)
        for k in range(1, n + 1):
            c += math.gcd(d, k)
print(c)
