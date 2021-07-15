import os
import sys

import numpy as np
from scipy.optimize import fmin

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")

N = int(sys.stdin.readline())
X, Y, D = list(zip(*[sys.stdin.readline().rstrip().split() for _ in range(N)]))
X = np.array(X, dtype=int)
Y = np.array(Y, dtype=int)
D = np.array(D)

Rmin = min(list(X[D == 'R']) + [INF])
Rmax = max(list(X[D == 'R']) + [-INF])
Lmin = min(list(X[D == 'L']) + [INF])
Lmax = max(list(X[D == 'L']) + [-INF])
Umin = min(list(Y[D == 'U']) + [INF])
Umax = max(list(Y[D == 'U']) + [-INF])
Dmin = min(list(Y[D == 'D']) + [INF])
Dmax = max(list(Y[D == 'D']) + [-INF])

Xmin = min(list(X[(D == 'U') | (D == 'D')]) + [INF])
Xmax = max(list(X[(D == 'U') | (D == 'D')]) + [-INF])
Ymin = min(list(Y[(D == 'R') | (D == 'L')]) + [INF])
Ymax = max(list(Y[(D == 'R') | (D == 'L')]) + [-INF])


def cost(t):
    if t < 0:
        return -t + 10 ** 18
    xl = min(Xmin, Lmin - t, Rmin + t)
    xr = max(Xmax, Lmax - t, Rmax + t)
    yb = min(Ymin, Dmin - t, Umin + t)
    yt = max(Ymax, Dmax - t, Umax + t)
    return (xr - xl) * (yt - yb)


x, = fmin(cost, x0=100000, ftol=10 ** -10, disp=False)
print(('{:.10f}'.format(cost(x))))

