import math
(a, b) = list(map(int, input().split()))
print(min(a, b), int(math.floor(abs(a - b) / 2)))
