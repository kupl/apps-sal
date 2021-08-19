import math
(N, r) = list(map(int, input().split()))
print(r * math.sin(math.pi / N) / (1 - math.sin(math.pi / N)))
