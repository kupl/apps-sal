import math
N, K = input().split()
N = int(N)
K = int(K)
if N == K:
    print(1)
else:
    print(math.ceil((N - K) / (K - 1)) + 1)
