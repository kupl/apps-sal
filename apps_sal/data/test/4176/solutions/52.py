import math
(a, b) = list(map(int, input().split()))
x = math.gcd(a, b)
y = a * b
ans = y // x
print(ans)
