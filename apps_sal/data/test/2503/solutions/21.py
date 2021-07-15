import numpy as np

N, K = map(int, input().split())
K2 = 2 * K
Mij = [[0 for _ in range(K2 + 1)] for _ in range(K2 + 1)]


def imos(x1, y1, x2, y2):
    Mij[y1][x1] += 1
    Mij[y2][x2] += 1
    Mij[y2][x1] -= 1
    Mij[y1][x2] -= 1

for _ in range(N):
    ls = input().split()
    x = int(ls[0]) % K2
    y = int(ls[1]) % K2
    if ls[2] == "B":
        y = (y + K) % K2
    x_ = x % K
    y_ = y % K

    if (x < K and y < K) or (K <= x and K <= y):
        imos(0, 0, x_ + 1, y_ + 1)
        imos(x_ + K + 1, 0, K2, y_ + 1)
        imos(0, y_ + K + 1, x_ + 1, K2)
        imos(x_ + K + 1, y_ + K + 1, K2, K2)
        imos(x_ + 1, y_ + 1, x_ + K + 1, y_ + K + 1)
    else:
        imos(x_ + 1, 0, x_ + K + 1, y_ + 1)
        imos(x_ + 1, y_ + K + 1, x_ + K + 1, K2)
        imos(0, y_ + 1, x_ + 1, y_ + K + 1)
        imos(x_ + K + 1, y_ + 1, K2, y_ + K + 1)

Mij = np.array(Mij)
for x in range(K2):
    Mij[:, x + 1] += Mij[:, x]
for y in range(K2):
    Mij[y + 1, :] += Mij[y, :]

print(Mij.max())
