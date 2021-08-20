import math
k = int(input())
s = 0
result = 0
for a in range(1, k + 1, 1):
    for b in range(a, k + 1, 1):
        for c in range(b, k + 1, 1):
            gcd = math.gcd(math.gcd(a, b), math.gcd(b, c))
            if a == b == c:
                pass
            elif a == b and b != c or (b == c and b != a) or (a == c and a != c):
                gcd = 3 * gcd
            else:
                gcd = 6 * gcd
            result += gcd
print(result)
