import math
(x, y, z) = map(int, input().split())
print(int(math.floor((x - z) / (y + z))))
