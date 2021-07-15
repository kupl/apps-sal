from scipy.optimize import fmin
INF = 10**18
n = int(input())
# 0:static, 1:up, 2:down
xpoints = [[] for _ in range(3)]
ypoints = [[] for _ in range(3)]
for i in range(n):
    x, y, d = [item for item in input().split()]
    x = int(x); y = int(y)
    if d == "R":
        ypoints[0].append(y)
        xpoints[1].append(x)
    elif d == "L":
        ypoints[0].append(y)
        xpoints[2].append(x)
    elif d == "U":
        xpoints[0].append(x)
        ypoints[1].append(y)
    elif d == "D":
        xpoints[0].append(x)
        ypoints[2].append(y)
for i in range(3):
    xpoints[i].sort()
    ypoints[i].sort()

def f(t):
    if t < 0:
        return INF 
    max_x = max_y = -INF
    min_x = min_y = INF
    for i, a in enumerate([0, t, -t]):
        if not len(xpoints[i]) == 0:
            max_x = max(max_x, xpoints[i][-1] + a)
            min_x = min(min_x, xpoints[i][0] + a)
        if not len(ypoints[i]) == 0:
            max_y = max(max_y, ypoints[i][-1] + a)
            min_y = min(min_y, ypoints[i][0] + a)
    return (max_x - min_x) * (max_y - min_y)

ans = fmin(f, x0=10**8, ftol= 1e-9, disp=False)
print(f(ans[0]))
