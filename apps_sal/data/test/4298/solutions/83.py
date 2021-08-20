import math
(n, d) = (int(i) for i in input().split())
print(math.ceil(n / (d * 2 + 1)))
