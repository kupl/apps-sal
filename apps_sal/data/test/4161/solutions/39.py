import math

k = int(input())
ans = 0
for a in range(1, k+1):
    for b in range(a+1, k+1):
        ans += math.gcd(a, b)
        for c in range(b+1, k+1):
            ans += math.gcd(math.gcd(a, b), c)
ans *= 6
ans += (k+1)*k/2
print((int(ans)))

