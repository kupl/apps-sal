import math
(n, d) = list(map(int, input().split()))
print(math.ceil(n / (2 * d + 1)))
