import math
n, m = map(int, input().split())
a = []
for i in range(m):
    d, h = map(int, input().split())
    a.append([d, h])
max_ = -1
c1 = 0
g = (a[0][0] - 1) + a[0][1]
if (g > max_):
    max_ = g
for i in range(len(a) - 1):
    g = math.floor(((a[i + 1][0] - a[i][0]) + a[i][1] + a[i + 1][1]) / 2)
    if ((a[i][1] > g) or (a[i + 1][1] > g)):
        c1 = -1
        break
    else:
        if (g > max_):
            max_ = g
g = (n - a[len(a) - 1][0]) + a[len(a) - 1][1]
if (g > max_):
    max_ = g
if (c1 != -1):
    print(max_)
else:
    print('IMPOSSIBLE')
