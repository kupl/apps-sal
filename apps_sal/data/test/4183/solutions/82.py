import math

n = int(input())
ans = 1
for _ in range(n):
    t = int(input())
    ans = ans * t // math.gcd(ans, t)
print(ans)
