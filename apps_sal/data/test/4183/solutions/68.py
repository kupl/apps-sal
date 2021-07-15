import math

n = int(input())
ans = 1
for _ in range(n):
    t1 = int(input())
    ans = ans//math.gcd(ans, t1)*t1

print(ans)
