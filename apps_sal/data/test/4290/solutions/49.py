import math
N, M = list(map(int, input().split()))

x = (N * (N - 1) / 2) + (M * (M - 1) / 2)

print((math.floor(x)))
