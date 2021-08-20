import math
(a, b) = map(int, input().split())
print(int(a / math.gcd(a, b) * b))
