from math import gcd
n = int(input())
ans = int(input())
for _ in range(n - 1):
    t = int(input())
    ans = (ans * t) // gcd(ans, t)

print(ans)
