import math

k = int(input())
wa = 0
aa = 0
for i in range(1, k + 1):
    for j in range(1, k + 1):
        aa = math.gcd(i, j)
        for l in range(1, k + 1):
            wa += math.gcd(aa, l)
print(wa)
