import numpy as np
from scipy.special import comb
n, d = map(int, input().split())
x = []
total = 0
for i in range(n):
    x.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if i != j:
            a = np.array(x[i])
            b = np.array(x[j])
            u = b - a
            if np.linalg.norm(u) == int(np.linalg.norm(u)):
                total += 1
print(int(total / 2))
