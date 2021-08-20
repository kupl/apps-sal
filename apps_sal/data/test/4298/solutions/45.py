import math
(N, D) = list(map(int, input().split()))
print(math.ceil(N / (D * 2 + 1)))
