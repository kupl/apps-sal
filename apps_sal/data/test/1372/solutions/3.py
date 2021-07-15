import numpy as np

h, n = list(map(int, input().split()))
la, lb = [], []
for _ in range(n):
    a, b = list(map(int, input().split()))
    la.append(a)
    lb.append(b)

aa = np.array(la)
ab = np.array(lb)
maxa = np.max(aa)

# min_magic[maxa + i] = min magic power to give damage >= i
min_magic = np.zeros(maxa + h + 1, int)

for i in range(1, h + 1):
    min_magic[maxa + i] = np.min(min_magic[maxa + i - la] + lb)

answer = min_magic[maxa + h]
print(answer)

