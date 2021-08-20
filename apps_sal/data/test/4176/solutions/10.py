import math
(a, b) = map(int, input().split())
c = math.gcd(a, b)
ans = a * b // c
print(ans)
