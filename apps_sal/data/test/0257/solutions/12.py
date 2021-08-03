import numpy as np
from scipy.optimize import fmin

n, k = list(map(int, input().split()))
XYC = [list(map(int, input().split())) for i in range(n)]
X, Y, C = [], [], []
for x, y, c in XYC:
    X.append(x)
    Y.append(y)
    C.append(c)
X = np.array(X, dtype=np.float)
Y = np.array(Y, dtype=np.float)
C = np.array(C, dtype=np.float)


def f(xy):
    x, y = xy
    times = (X - x) * (X - x) + (Y - y) * (Y - y)
    times = C * np.sqrt(times)
    times = np.sort(times)
    return times[k - 1]


deff = 0.5
ansx = [fmin(f, (x, y), disp=False, ftol=10**(-7), initial_simplex=[(x + deff, y), (x - deff, y + deff), (x - deff, y - deff)]) for x, y, c in XYC]
ansy = list([f(x) for x in ansx])
print((min(ansy)))
