import math
K = int(input())
ans = 0

for a in range(1, K + 1):
    for b in range(a, K + 1):
        for c in range(b, K + 1):
            s = math.gcd(a, b)
            t = math.gcd(s, c)
            if a == c:
                ans += t
            elif (a == b or b == c) and a != c:
                ans += 3 * t
            else:
                ans += 6 * t
print(ans)
