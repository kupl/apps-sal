import math
N, M = map(int, input().split())
print((M + N) * (M + N - 1) // 2 - M * N)
