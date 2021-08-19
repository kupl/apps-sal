import math
k = int(input())
ans = 0
for a in range(1, k + 1):
    for b in range(a, k + 1):
        for c in range(b, k + 1):
            gcd = math.gcd(math.gcd(a, b), c)
            if a == b == c:
                ans += gcd
            elif a == b or b == c:
                ans += gcd * 3
            else:
                ans += gcd * 6
print(ans)
