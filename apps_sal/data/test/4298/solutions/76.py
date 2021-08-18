import math
N, D = map(int, input().split())
print(int(math.ceil(N / (2 * D + 1))))
