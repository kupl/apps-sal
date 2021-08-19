import math
k = int(input())
s = 0
for a in range(1, k + 1):
    for b in range(1, k + 1):
        gcdab = math.gcd(a, b)
        if gcdab == 1:
            s += k
        else:
            for c in range(1, k + 1):
                s += math.gcd(gcdab, c)
print(s)
