import itertools
import numpy as np
N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]
count = 0
for i in itertools.combinations(X, 2):
    if np.linalg.norm(list(map(lambda x, y: abs(x - y), i[0], i[1]))) % 1 == 0: count += 1
print(count)
