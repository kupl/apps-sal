import numpy as np

n, m, c = map(int, input().split())
b = list(map(int, input().split()))
b = np.array(b)
tot = 0

for _ in range(n):
    a = list(map(int, input().split()))
    a = np.array(a)
    if np.dot(a, b) + c > 0:
        tot += 1

print(tot)
