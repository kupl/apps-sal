import math
(n, m, a, b) = map(int, input().split())
print(min(math.floor(n / m) * b + n % m * a, (math.floor(n / m) + 1) * b, a * n))
