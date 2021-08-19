import numpy as np
import math


def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(map(int, input().split()))


n = ii()
a = []
for i in range(n):
    (x, y) = mi()
    x += 1e-15
    theta = math.degrees(math.atan2(y, x))
    a.append([theta, x, y])
a.sort()
a2 = list(a)
a = a + a2
x = []
y = []
for i in range(len(a)):
    x.append(a[i][1])
    y.append(a[i][2])
x = np.array(x)
y = np.array(y)
xsum = np.cumsum(x)
ysum = np.cumsum(y)
ans = 0
for i in range(1, n + 1):
    for k in range(i, n + i):
        xtmp = xsum[k] - xsum[i - 1]
        ytmp = ysum[k] - ysum[i - 1]
        tmp = (xtmp ** 2 + ytmp ** 2) ** 0.5
        ans = max(ans, tmp)
print(ans)
