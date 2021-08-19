import math
(N, D) = map(int, input().split())
hani = N + D - (N - D) + 1
print(math.ceil(N / hani))
