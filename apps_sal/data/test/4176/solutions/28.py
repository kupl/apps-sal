import math
(a, b) = map(int, input().split())
div = math.gcd(a, b)
print(div * a // div * b // div)
