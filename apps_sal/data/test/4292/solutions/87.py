import numpy as np
N, K = map(int, input().split())
p = list(map(int, input().split()))

print(np.sum(sorted(p)[:K]))
