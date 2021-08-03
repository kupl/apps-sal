import numpy as np
n, c = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

a = np.zeros((c + 1, 10**5))

for i in range(n):
    a[ab[i][2]][(ab[i][0] - 1):ab[i][1]] = [1] * (ab[i][1] - ab[i][0] + 1)

b = a.sum(axis=0)

print(int(max(b)))
