import numpy as np

L, A, B, M = (int(i) for i in input().split())
keta = [0] * 18
for i in range(18):
    keta[i] = min((10**i - A - 1) // B, L - 1)
keta.reverse()
for i in range(18):
    if keta[i] < 0:
        keta[i] = -1
        break
keta.reverse()


def power(g, N, M):
    if N == 0:
        g = np.array([1, 0, 0, 0, 1, 0, 0, 0, 1]).reshape(3, 3)
    elif N == 1:
        pass
    elif N % 2 == 0:
        g = np.linalg.matrix_power(power(g, N // 2, M), 2)
    elif N % 2 == 1:
        g = np.dot(g, power(g, N - 1, M))
    return g % M


ans = 0
for i in range(18):
    N = i + 1
    mi = keta[i] + 1
    if mi < 0:
        continue
    if i != 17:
        ma = keta[i + 1]
    else:
        ma = L - 1
    if mi >= L:
        break
    t = np.array([ans, (A + B * mi) % M, 1])
    g = np.array([10**N % M, 0, 0, 1, 1, 0, 0, B % M, 1]).reshape(3, 3)
    g = power(g, ma - mi + 1, M)
    g = np.dot(t, g)
    ans = g[0] % M
print(ans)
