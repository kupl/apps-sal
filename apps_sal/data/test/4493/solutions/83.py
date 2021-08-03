import numpy as np

M = np.array(list(map(int, open(0).read().split()))).reshape(3, 3)

hSum = M.sum(axis=0)
vSum = M.sum(axis=1)

f = True
for i in range(3):
    if (hSum[i] - hSum[(i + 1) % 3]) % 3 != 0:
        f = False

for i in range(3):
    if (vSum[i] - vSum[(i + 1) % 3]) % 3 != 0:
        f = False

print("Yes" if f else "No")
