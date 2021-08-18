import numpy as np
from collections import defaultdict

h, w, m = map(int, input().split())

rowsum = np.zeros(h, dtype=int)
colsum = np.zeros(w, dtype=int)
targets = defaultdict(int)
for _ in range(m):
    hi, wi = map(int, input().split())
    hi -= 1
    wi -= 1
    rowsum[hi] += 1
    colsum[wi] += 1
    targets[(hi, wi)] = 1

rowmax = np.max(rowsum)
colmax = np.max(colsum)
rowindices = np.where(rowsum == rowmax)[0]
colindices = np.where(colsum == colmax)[0]

for ri in rowindices:
    for ci in colindices:
        if targets[(ri, ci)]:
            continue
        print(rowmax + colmax)
        return

print(rowmax + colmax - 1)
