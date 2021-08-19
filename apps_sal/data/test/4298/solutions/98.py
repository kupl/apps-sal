import math
(n, d) = list(map(int, input().split()))
scope = d * 2 + 1
print(math.ceil(n / scope))
