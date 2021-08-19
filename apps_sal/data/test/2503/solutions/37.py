import sys
import numpy as np
from collections import Counter
read = sys.stdin
(N, K) = list(map(int, read.readline().split()))
k = 2 * K
xyc = np.array(read.read().split(), np.str).reshape(-1, 3)
x = xyc[:, 0].astype(int)
y = xyc[:, 1].astype(int)
c = xyc[:, 2]
x[c == 'B'] -= K
x %= k
y %= k
grid = np.zeros((3 * K, 3 * K), np.int64)
np.add.at(grid, (x, y), 1)
np.add.at(grid, (x + K, y + K), 1)
np.subtract.at(grid, (x + K, y), 1)
np.subtract.at(grid, (x, y + K), 1)
np.cumsum(grid, axis=0, out=grid)
np.cumsum(grid, axis=1, out=grid)
p1 = grid[:K, :K] + grid[k:, k:] + grid[K:k, K:k] + grid[k:, :K] + grid[:K, k:]
p2 = grid[K:k, :K] + grid[K:k, k:] + grid[:K, K:k] + grid[k:, K:k]
print(max(p1.max(), p2.max()))
