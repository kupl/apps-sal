import numpy as np
N, K = list(map(int, input().split()))
cum = [[0] * (2 * K + 1) for i in range(2 * K + 1)]


def vertex(z):
    if z < K:
        return [(0, z + 1), (z + K + 1, 2 * K)]
    else:
        return [(z - K + 1, z + 1)]


for i in range(N):
    x, y, c = input().split()
    x = int(x)
    y = int(y)
    x %= 2 * K
    if c == 'B':
        y %= 2 * K
    else:
        y += K
        y %= 2 * K

    for d in [0, K]:
        for b, t in vertex((y + d) % (2 * K)):
            for l, r in vertex((x + d) % (2 * K)):
                cum[b][l] += 1
                cum[t][r] += 1
                cum[b][r] -= 1
                cum[t][l] -= 1

cum = np.array(cum)
print((np.cumsum(np.cumsum(cum, axis=0), axis=1).max()))
