import math
k = int(input())
ans = 0
for a in range(1, k + 1):
    for b in range(a, k + 1):
        for c in range(b, k + 1):
            if a == b == c:
                ans += math.gcd(math.gcd(a, b), c)
            elif a == b or b == c or c == a:
                ans += 3 * math.gcd(math.gcd(a, b), c)
            else:
                ans += 6 * math.gcd(math.gcd(a, b), c)
print(ans)
