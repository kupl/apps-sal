import numpy as np

N, K = map(int, input().split())
h = np.array(list(map(int, input().split())))

print(np.sum(h >= K))
