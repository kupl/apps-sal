import math
N, K, *A = map(int, open(0).read().split())

print(int(math.ceil((N - 1) / (K - 1))))
