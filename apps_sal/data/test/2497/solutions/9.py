import numpy as np
from scipy.optimize import fmin

INF = 10**18

mapping = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1)
}


def f(x, vx, t):
    if t < 0:
        return INF
    nx = x + vx * t
    return nx.max() - nx.min()


def solve(n, x, y, d):
    x = np.asarray(x, dtype=np.float)
    y = np.asarray(y, dtype=np.float)
    vx = np.zeros(n, dtype=np.float)
    vy = np.zeros(n, dtype=np.float)
    for i in range(n):
        vx[i], vy[i] = mapping[d[i]]
    h = lambda t: f(y, vy, t) * f(x, vx, t)
    t = fmin(h, x0=10**8, ftol=1e-9, disp=False)[0]
    return h(t)


n = int(input())
x, y, d = [-1] * n, [-1] * n, [-1] * n
for i in range(n):
    x[i], y[i], d[i] = input().split()
    x[i] = int(x[i])
    y[i] = int(y[i])
print(solve(n, x, y, d))
