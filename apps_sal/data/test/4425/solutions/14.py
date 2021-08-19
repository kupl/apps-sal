# Answer
import math
N, K = input().split()
N = int(N)
K = int(K)

M = math.log(K, 2)
P = sum([1 / (2**max(math.ceil(M - math.log(i, 2)), 0)) for i in range(1, N + 1)]) / N
print(P)
