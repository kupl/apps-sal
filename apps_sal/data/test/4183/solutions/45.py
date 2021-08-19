import math
n = int(input())
ans = 1
for i in range(n):
    t = int(input())
    ans = ans // math.gcd(ans, t) * t
print(ans)
