import math


n = int(input())
a = list(map(int, input().split()))

gcd_l = [0] * (n + 1)
gcd_r = [0] * (n + 1)

for i in range(n):
    gcd_l[i + 1] = math.gcd(gcd_l[i], a[i])
    gcd_r[n - i - 1] = math.gcd(gcd_r[n - i], a[n - i - 1])

ans = 1
for l, r in zip(gcd_l, gcd_r[1:]):
    ans = max(ans, math.gcd(l, r))

print(ans)
